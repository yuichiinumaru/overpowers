#!/usr/bin/env python3
"""
A股K线图分析器 - 使用新浪财经API获取实时数据，Baostock获取K线数据
功能：获取K线数据、计算技术指标、生成图表
"""

import argparse
import json
import sys
import requests
import time
from datetime import datetime, timedelta

try:
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    from matplotlib.patches import Rectangle
    PLOTTING_AVAILABLE = True
except ImportError as e:
    print(f"警告：部分依赖未安装: {e}")
    PLOTTING_AVAILABLE = False


class SinaFinanceAPI:
    """新浪财经API封装 - 实时价格"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Referer': 'https://finance.sina.com.cn',
            'Connection': 'keep-alive',
        })
    
    def _get_sina_code(self, code: str) -> str:
        """转换为新浪股票代码格式
        
        上海：600/601/603/605/688（科创板）开头 -> sh
        深圳：000/001/002/003（主板/中小板）开头 -> sz
        创业板：300/301开头 -> sz
        北交所：430/830/87开头 -> bj（暂不支持）
        """
        code = code.strip()
        # 上海股票（包括科创板688）
        if code.startswith(('6', '688')):
            return f"sh{code}"
        # 深圳股票（包括创业板300/301）
        elif code.startswith(('0', '3')):
            return f"sz{code}"
        # 北交所（bj）暂不支持，按上海处理
        elif code.startswith(('4', '8')):
            return f"bj{code}"
        else:
            # 默认深圳
            return f"sz{code}"
    
    def get_realtime_price(self, code: str) -> dict:
        """获取实时价格"""
        time.sleep(0.3)
        try:
            sina_code = self._get_sina_code(code)
            url = f'https://hq.sinajs.cn/list={sina_code}'
            response = self.session.get(url, timeout=10)
            
            if response.status_code != 200:
                return None
            
            content = response.text
            if not content or '=""' in content:
                return None
            
            data_str = content.split('="')[1].split('"')[0]
            parts = data_str.split(',')
            
            if len(parts) < 33:
                return None
            
            return {
                'code': code,
                'name': parts[0],
                'open': float(parts[1]),
                'prev_close': float(parts[2]),
                'price': float(parts[3]),
                'high': float(parts[4]),
                'low': float(parts[5]),
                'volume': int(parts[8]),
                'amount': float(parts[9]),
                'change': float(parts[3]) - float(parts[2]),
                'change_pct': (float(parts[3]) - float(parts[2])) / float(parts[2]) * 100 if float(parts[2]) > 0 else 0,
                'time': f"{parts[30]} {parts[31]}",
                'bid1_price': float(parts[11]),
                'bid1_volume': int(parts[10]),
                'ask1_price': float(parts[21]),
                'ask1_volume': int(parts[20]),
            }
        except Exception as e:
            print(f"获取实时价格失败: {e}")
            return None


class BaostockAPI:
    """Baostock API封装 - K线数据"""
    
    def __init__(self):
        self.bs = None
        self._login()
    
    def _login(self):
        """登录Baostock"""
        try:
            import baostock as bs
            self.bs = bs
            lg = bs.login()
            if lg.error_code != '0':
                print(f"Baostock登录失败: {lg.error_msg}")
        except ImportError:
            print("Baostock未安装，请运行: pip3 install baostock")
    
    def _get_bs_code(self, code: str) -> str:
        """转换为Baostock代码格式
        
        上海：600/601/603/605/688开头 -> sh.
        深圳：000/001/002/003开头 -> sz.
        创业板：300/301开头 -> sz.
        """
        code = code.strip()
        # 上海股票（包括科创板688）
        if code.startswith(('6', '688')):
            return f"sh.{code}"
        # 深圳股票（包括主板、中小板、创业板300/301）
        elif code.startswith(('0', '3')):
            return f"sz.{code}"
        else:
            # 默认深圳
            return f"sz.{code}"
    
    def get_kline_data(self, code: str, period: str = "daily", days: int = 60) -> pd.DataFrame:
        """获取K线数据"""
        if not self.bs:
            print("Baostock未初始化")
            return None
        
        try:
            bs_code = self._get_bs_code(code)
            end_date = datetime.now().strftime('%Y-%m-%d')
            start_date = (datetime.now() - timedelta(days=days*2)).strftime('%Y-%m-%d')
            
            # 转换周期
            freq_map = {'daily': 'd', 'weekly': 'w', 'monthly': 'm'}
            freq = freq_map.get(period, 'd')
            
            rs = self.bs.query_history_k_data_plus(
                bs_code,
                "date,code,open,high,low,close,preclose,volume,amount,turn,pctChg",
                start_date=start_date, end_date=end_date, frequency=freq, adjustflag="3"
            )
            
            if rs.error_code != '0':
                print(f"获取K线数据失败: {rs.error_msg}")
                return None
            
            data_list = []
            while (rs.error_code == '0') & rs.next():
                data_list.append(rs.get_row_data())
            
            if not data_list:
                return None
            
            df = pd.DataFrame(data_list, columns=rs.fields)
            
            # 转换数据类型
            numeric_cols = ['open', 'high', 'low', 'close', 'preclose', 'volume', 'amount', 'turn', 'pctChg']
            for col in numeric_cols:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce')
            
            # 重命名列以兼容原有代码
            df = df.rename(columns={
                'date': 'date',
                'open': 'open',
                'high': 'high',
                'low': 'low',
                'close': 'close',
                'volume': 'volume',
                'amount': 'amount',
                'turn': 'turnover',
                'pctChg': 'change_pct'
            })
            
            # 计算涨跌额
            df['change'] = df['close'] - df['preclose']
            
            # 取最近days条
            df = df.tail(days).reset_index(drop=True)
            
            return df
            
        except Exception as e:
            print(f"获取K线数据异常: {e}")
            return None
    
    def __del__(self):
        """析构时登出"""
        if self.bs:
            try:
                self.bs.logout()
            except:
                pass


class StockDataSource:
    """股票数据源管理器 - 整合新浪财经(实时) + Baostock(K线)"""
    
    def __init__(self):
        self.realtime_api = SinaFinanceAPI()
        self.kline_api = BaostockAPI()
    
    def get_realtime_price(self, code: str) -> dict:
        """获取实时价格"""
        return self.realtime_api.get_realtime_price(code)
    
    def get_kline_data(self, code: str, period: str = "daily", days: int = 60) -> pd.DataFrame:
        """获取K线数据"""
        return self.kline_api.get_kline_data(code, period, days)


def calculate_ma(df, periods=[5, 10, 20, 60]):
    """计算移动平均线"""
    for period in periods:
        df[f'MA{period}'] = df['close'].rolling(window=period).mean()
    return df


def calculate_macd(df, fast=12, slow=26, signal=9):
    """计算MACD指标"""
    ema_fast = df['close'].ewm(span=fast, adjust=False).mean()
    ema_slow = df['close'].ewm(span=slow, adjust=False).mean()
    df['MACD'] = ema_fast - ema_slow
    df['MACD_Signal'] = df['MACD'].ewm(span=signal, adjust=False).mean()
    df['MACD_Hist'] = df['MACD'] - df['MACD_Signal']
    return df


def calculate_rsi(df, period=14):
    """计算RSI指标"""
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df


def calculate_bollinger(df, period=20, std_dev=2):
    """计算布林带"""
    df['BOLL_MID'] = df['close'].rolling(window=period).mean()
    df['BOLL_STD'] = df['close'].rolling(window=period).std()
    df['BOLL_UP'] = df['BOLL_MID'] + (df['BOLL_STD'] * std_dev)
    df['BOLL_DOWN'] = df['BOLL_MID'] - (df['BOLL_STD'] * std_dev)
    return df


def identify_patterns(df):
    """识别K线形态"""
    patterns = []
    
    for i in range(1, len(df)):
        row = df.iloc[i]
        prev_row = df.iloc[i-1]
        
        body = abs(row['close'] - row['open'])
        lower_shadow = min(row['open'], row['close']) - row['low']
        upper_shadow = row['high'] - max(row['open'], row['close'])
        total_range = row['high'] - row['low']
        
        if total_range == 0:
            continue
        
        # 锤子线
        if lower_shadow > body * 2 and upper_shadow < body * 0.5 and body > 0:
            patterns.append({
                'date': row['date'],
                'pattern': '锤子线',
                'signal': '看涨' if row['close'] > row['open'] else '看跌',
                'price': row['close']
            })
        
        # 十字星
        if body < total_range * 0.1 and total_range > 0:
            patterns.append({
                'date': row['date'],
                'pattern': '十字星',
                'signal': '反转信号',
                'price': row['close']
            })
        
        # 看涨吞没
        if (prev_row['close'] < prev_row['open'] and
            row['close'] > row['open'] and
            row['open'] < prev_row['close'] and
            row['close'] > prev_row['open']):
            patterns.append({
                'date': row['date'],
                'pattern': '看涨吞没',
                'signal': '强烈看涨',
                'price': row['close']
            })
        
        # 看跌吞没
        if (prev_row['close'] > prev_row['open'] and
            row['close'] < row['open'] and
            row['open'] > prev_row['close'] and
            row['close'] < prev_row['open']):
            patterns.append({
                'date': row['date'],
                'pattern': '看跌吞没',
                'signal': '强烈看跌',
                'price': row['close']
            })
    
    return patterns[-10:]


def plot_kline(df, stock_code, stock_name='', save_path=None):
    """绘制K线图"""
    if not PLOTTING_AVAILABLE:
        print("绘图功能不可用，请安装 matplotlib")
        return
    
    fig, axes = plt.subplots(3, 1, figsize=(14, 10),
                            gridspec_kw={'height_ratios': [3, 1, 1]})
    ax1, ax2, ax3 = axes
    
    df['date'] = pd.to_datetime(df['date'])
    x_range = range(len(df))
    
    # 绘制K线
    for idx, row in df.iterrows():
        color = 'red' if row['close'] >= row['open'] else 'green'
        height = abs(row['close'] - row['open'])
        bottom = min(row['close'], row['open'])
        if height < 0.01:
            height = 0.01
        rect = Rectangle((idx-0.3, bottom), 0.6, height,
                        facecolor=color, edgecolor=color, linewidth=0.5)
        ax1.add_patch(rect)
        ax1.plot([idx, idx], [row['low'], row['high']],
                color=color, linewidth=0.8)
    
    # 均线
    colors_ma = {'MA5': 'orange', 'MA10': 'blue', 'MA20': 'purple', 'MA60': 'gray'}
    for ma, color in colors_ma.items():
        if ma in df.columns and not df[ma].isna().all():
            ax1.plot(x_range, df[ma], label=ma, color=color, linewidth=1.2, alpha=0.8)
    
    # 布林带
    if 'BOLL_UP' in df.columns:
        ax1.plot(x_range, df['BOLL_UP'], label='BOLL_UP',
                color='gray', linestyle='--', linewidth=0.8, alpha=0.6)
        ax1.plot(x_range, df['BOLL_MID'], label='BOLL_MID',
                color='gray', linestyle='-', linewidth=0.8, alpha=0.6)
        ax1.plot(x_range, df['BOLL_DOWN'], label='BOLL_DOWN',
                color='gray', linestyle='--', linewidth=0.8, alpha=0.6)
        ax1.fill_between(x_range, df['BOLL_UP'], df['BOLL_DOWN'],
                        alpha=0.1, color='gray')
    
    title = f'{stock_code} {stock_name} K线图' if stock_name else f'{stock_code} K线图'
    ax1.set_title(title, fontsize=14, fontweight='bold')
    ax1.set_ylabel('价格', fontsize=10)
    ax1.legend(loc='upper left', fontsize=8)
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.set_xlim(-0.5, len(df)-0.5)
    
    step = max(1, len(df) // 10)
    ax1.set_xticks(range(0, len(df), step))
    ax1.set_xticklabels([df.iloc[i]['date'].strftime('%m-%d')
                         for i in range(0, len(df), step)], rotation=45)
    
    # 成交量
    colors_vol = ['red' if df.iloc[i]['close'] >= df.iloc[i]['open'] else 'green'
                  for i in range(len(df))]
    ax2.bar(x_range, df['volume'], color=colors_vol, alpha=0.7, width=0.8)
    ax2.set_ylabel('成交量', fontsize=10)
    ax2.grid(True, alpha=0.3, linestyle='--')
    ax2.set_xlim(-0.5, len(df)-0.5)
    
    # MACD
    if 'MACD' in df.columns:
        ax3.plot(x_range, df['MACD'], label='MACD', color='blue', linewidth=1)
        ax3.plot(x_range, df['MACD_Signal'], label='Signal',
                color='orange', linewidth=1)
        macd_colors = ['red' if df.iloc[i]['MACD_Hist'] > 0 else 'green'
                      for i in range(len(df))]
        ax3.bar(x_range, df['MACD_Hist'], color=macd_colors, alpha=0.6, width=0.8)
        ax3.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
        ax3.set_ylabel('MACD', fontsize=10)
        ax3.legend(loc='upper left', fontsize=8)
        ax3.grid(True, alpha=0.3, linestyle='--')
        ax3.set_xlim(-0.5, len(df)-0.5)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"图表已保存: {save_path}")
    else:
        plt.show()
    
    plt.close()


def generate_report(df, patterns, realtime_data, stock_code):
    """生成技术分析报告 - 增强版，包含详细判断依据和名词解释"""
    latest = df.iloc[-1]
    prev = df.iloc[-2] if len(df) > 1 else latest
    
    if realtime_data:
        current_price = realtime_data['price']
        change_pct = realtime_data['change_pct']
        change = realtime_data['change']
    else:
        current_price = latest['close']
        change_pct = latest['change_pct']
        change = latest['change']
    
    report = f"""
{'='*60}
📊 {stock_code} {realtime_data.get('name', '') if realtime_data else ''} 技术分析报告
{'='*60}
分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

【实时行情】
最新价: {current_price:.2f} 元
涨跌幅: {change_pct:+.2f}% ({change:+.2f}元)
开盘价: {realtime_data['open'] if realtime_data else latest['open']:.2f} 元
最高价: {realtime_data['high'] if realtime_data else latest['high']:.2f} 元
最低价: {realtime_data['low'] if realtime_data else latest['low']:.2f} 元
昨收价: {realtime_data['prev_close'] if realtime_data else prev['close']:.2f} 元
成交量: {realtime_data['volume']/10000 if realtime_data else latest['volume']/10000:.2f} 万手
成交额: {realtime_data['amount']/10000 if realtime_data else latest['amount']/10000:.2f} 万元
更新时间: {realtime_data['time'] if realtime_data else 'N/A'}

【技术指标详解】
"""
    
    # 移动平均线详细说明
    report += "\n1️⃣ 移动平均线 (MA)\n"
    report += "   含义: 反映股价一段时间内的平均成本，判断趋势方向\n"
    for ma in ['MA5', 'MA10', 'MA20', 'MA60']:
        if ma in df.columns and not pd.isna(latest[ma]):
            status = "上方📈" if current_price > latest[ma] else "下方📉"
            # 判断均线趋势
            if len(df) >= 5 and not pd.isna(df.iloc[-5][ma]):
                ma_trend = "上升" if latest[ma] > df.iloc[-5][ma] else "下降" if latest[ma] < df.iloc[-5][ma] else "走平"
            else:
                ma_trend = "未知"
            report += f"   {ma}: {latest[ma]:.2f} (股价在其{status}，均线{ma_trend})\n"
    
    # RSI详细说明
    if 'RSI' in df.columns and not pd.isna(latest['RSI']):
        rsi = latest['RSI']
        rsi_status = "超买⚠️" if rsi > 70 else "超卖💡" if rsi < 30 else "中性➖"
        rsi_reason = "RSI>70表示买盘过强，可能回调" if rsi > 70 else "RSI<30表示卖盘过强，可能反弹" if rsi < 30 else "RSI在30-70之间，多空平衡"
        report += f"\n2️⃣ RSI相对强弱指标 (14日)\n"
        report += f"   含义: 衡量股价涨跌力度，0-100区间，判断超买超卖\n"
        report += f"   数值: {rsi:.2f} ({rsi_status})\n"
        report += f"   判断: {rsi_reason}\n"
    
    # MACD详细说明
    if 'MACD' in df.columns and not pd.isna(latest['MACD']):
        macd_val = latest['MACD']
        signal_val = latest['MACD_Signal']
        hist_val = latest['MACD_Hist']
        macd_status = "金叉📈" if macd_val > signal_val else "死叉📉"
        macd_reason = "MACD上穿Signal线，买入信号" if macd_val > signal_val else "MACD下穿Signal线，卖出信号"
        report += f"\n3️⃣ MACD指数平滑异同平均线\n"
        report += f"   含义: 通过快慢均线差值判断趋势转折和动能\n"
        report += f"   DIF(MACD): {macd_val:.3f}\n"
        report += f"   DEA(Signal): {signal_val:.3f}\n"
        report += f"   柱状图: {hist_val:.3f}\n"
        report += f"   状态: {macd_status} - {macd_reason}\n"
    
    # 布林带详细说明
    if 'BOLL_UP' in df.columns:
        boll_pos = "上轨附近⚠️" if current_price > latest['BOLL_UP'] * 0.98 else \
                   "下轨附近💡" if current_price < latest['BOLL_DOWN'] * 1.02 else "中轨附近➖"
        boll_reason = "触及上轨，可能超买回调" if current_price > latest['BOLL_UP'] * 0.98 else \
                      "触及下轨，可能超卖反弹" if current_price < latest['BOLL_DOWN'] * 1.02 else "在中轨附近，趋势延续"
        report += f"\n4️⃣ 布林带 (BOLL, 20日)\n"
        report += f"   含义: 通过标准差衡量股价波动区间，判断支撑压力\n"
        report += f"   上轨(压力): {latest['BOLL_UP']:.2f}\n"
        report += f"   中轨(均线): {latest['BOLL_MID']:.2f}\n"
        report += f"   下轨(支撑): {latest['BOLL_DOWN']:.2f}\n"
        report += f"   位置: {boll_pos} - {boll_reason}\n"
    
    report += "\n【K线形态识别】\n"
    report += "   含义: 通过单根或多根K线组合判断市场情绪和转折信号\n"
    if patterns:
        for p in patterns[-5:]:
            pattern_explain = {
                '锤子线': '下影线长，表示下方支撑强，可能反弹',
                '倒锤子': '上影线长，表示上方压力大，可能回落',
                '十字星': '多空力量均衡，可能变盘',
                '看涨吞没': '阳线包阴线，强烈看涨信号',
                '看跌吞没': '阴线包阳线，强烈看跌信号'
            }.get(p['pattern'], '特殊形态，需结合趋势判断')
            report += f"   {p['date']}: {p['pattern']} - {p['signal']}\n"
            report += f"            解释: {pattern_explain} @ {p['price']:.2f}\n"
    else:
        report += "   近期无明显K线形态\n"
    
    report += "\n【趋势判断】\n"
    report += "   判断方法: 通过均线排列和价格位置判断趋势方向\n"
    if 'MA5' in df.columns and 'MA20' in df.columns:
        ma5_trend = "向上" if latest['MA5'] > df.iloc[-5]['MA5'] else "向下"
        trend = "短期趋势: 上升 📈" if latest['MA5'] > latest['MA20'] else "短期趋势: 下降 📉"
        trend_reason = "MA5在MA20上方，短期强势" if latest['MA5'] > latest['MA20'] else "MA5在MA20下方，短期弱势"
        report += f"   {trend}\n"
        report += f"   依据: {trend_reason} (MA5 {ma5_trend})\n"
    
    if 'MA20' in df.columns and 'MA60' in df.columns:
        trend_long = "中长期趋势: 上升 📈" if latest['MA20'] > latest['MA60'] else "中长期趋势: 下降 📉"
        trend_long_reason = "MA20在MA60上方，中长期向好" if latest['MA20'] > latest['MA60'] else "MA20在MA60下方，中长期走弱"
        report += f"   {trend_long}\n"
        report += f"   依据: {trend_long_reason}\n"
    
    report += "\n【综合建议】\n"
    report += "   综合以上技术指标和形态，给出以下分析:\n\n"
    signals = []
    signal_weights = []
    
    if 'RSI' in df.columns:
        if latest['RSI'] < 30:
            signals.append("• RSI超卖(<30)，短期可能存在反弹机会，可考虑逢低关注")
            signal_weights.append(1)
        elif latest['RSI'] > 70:
            signals.append("• RSI超买(>70)，注意回调风险，可考虑适当减仓")
            signal_weights.append(-1)
    
    if 'MACD' in df.columns:
        if latest['MACD'] > latest['MACD_Signal']:
            signals.append("• MACD金叉，DIF上穿DEA，短期上涨动能增强，偏多信号")
            signal_weights.append(1)
        else:
            signals.append("• MACD死叉，DIF下穿DEA，短期下跌动能增强，偏空信号")
            signal_weights.append(-1)
    
    if 'BOLL_UP' in df.columns:
        if current_price > latest['BOLL_UP']:
            signals.append("• 股价突破布林带上轨，处于超买区域，注意回调风险")
            signal_weights.append(-0.5)
        elif current_price < latest['BOLL_DOWN']:
            signals.append("• 股价跌破布林带下轨，处于超卖区域，可能存在反弹机会")
            signal_weights.append(0.5)
    
    if patterns and patterns[-1]['signal'] in ['强烈看涨', '看涨']:
        signals.append(f"• 最近出现{patterns[-1]['pattern']}形态，技术信号偏多")
        signal_weights.append(1)
    elif patterns and patterns[-1]['signal'] in ['强烈看跌', '看跌']:
        signals.append(f"• 最近出现{patterns[-1]['pattern']}形态，技术信号偏空")
        signal_weights.append(-1)
    
    # 均线多头排列/空头排列
    if 'MA5' in df.columns and 'MA10' in df.columns and 'MA20' in df.columns:
        if latest['MA5'] > latest['MA10'] > latest['MA20']:
            signals.append("• 均线多头排列(MA5>MA10>MA20)，趋势向好，支撑有力")
            signal_weights.append(1)
        elif latest['MA5'] < latest['MA10'] < latest['MA20']:
            signals.append("• 均线空头排列(MA5<MA10<MA20)，趋势走弱，压力明显")
            signal_weights.append(-1)
    
    if signals:
        for s in signals:
            report += f"{s}\n"
    else:
        report += "• 暂无明确技术信号，建议观望或结合基本面分析\n"
    
    # 综合评分
    total_score = sum(signal_weights)
    report += f"\n   技术评分: {total_score:+.1f}分 (范围: -5到+5)\n"
    if total_score >= 3:
        report += "   综合判断: 🟢 强烈看多 - 多项指标共振向上\n"
    elif total_score >= 1:
        report += "   综合判断: 🟡 偏多 - 多数指标显示积极信号\n"
    elif total_score <= -3:
        report += "   综合判断: 🔴 强烈看空 - 多项指标共振向下\n"
    elif total_score <= -1:
        report += "   综合判断: 🟠 偏空 - 多数指标显示消极信号\n"
    else:
        report += "   综合判断: ⚪ 中性 - 多空力量均衡，方向不明\n"
    
    # 添加名词解释附录
    report += "\n" + "="*60
    report += "\n📚 技术指标名词解释\n"
    report += "="*60 + "\n"
    
    report += """
【移动平均线 MA】
  • 定义: 一定周期内收盘价的平均值连线
  • MA5: 5日均线，反映短期趋势
  • MA10: 10日均线，反映中短期趋势
  • MA20: 20日均线，反映中期趋势
  • MA60: 60日均线，反映长期趋势
  • 用法: 股价在均线上方看多，下方看空；均线多头排列看涨，空头排列看跌

【RSI相对强弱指标】
  • 定义: 通过比较一段时间内的平均涨幅和跌幅，衡量买卖力量对比
  • 范围: 0-100
  • RSI>70: 超买区域，可能回调
  • RSI<30: 超卖区域，可能反弹
  • RSI 30-70: 正常区域，趋势延续

【MACD指数平滑异同平均线】
  • DIF(快线): 12日EMA - 26日EMA
  • DEA(慢线/Signal): DIF的9日EMA
  • 柱状图: DIF - DEA
  • 金叉: DIF上穿DEA，买入信号
  • 死叉: DIF下穿DEA，卖出信号
  • 柱状图由负转正: 动能转强
  • 柱状图由正转负: 动能转弱

【布林带 BOLL】
  • 中轨: 20日均线
  • 上轨: 中轨 + 2倍标准差(压力位)
  • 下轨: 中轨 - 2倍标准差(支撑位)
  • 用法: 股价触及上轨可能回落，触及下轨可能反弹；带宽收窄预示变盘

【K线形态】
  • 锤子线: 下影线长，实体小，底部反转信号
  • 倒锤子: 上影线长，实体小，顶部反转信号
  • 十字星: 开盘价≈收盘价，多空均衡，变盘信号
  • 看涨吞没: 阳线包阴线，强烈看涨
  • 看跌吞没: 阴线包阳线，强烈看跌
"""
    
    report += "\n" + "="*60
    report += "\n⚠️ 免责声明\n"
    report += "="*60 + "\n"
    report += """
1. 以上分析仅基于技术指标，不构成投资建议
2. 技术分析有滞后性，不能预测突发事件
3. 投资有风险，入市需谨慎
4. 建议结合基本面分析和市场环境综合判断
"""
    
    return report


def main():
    parser = argparse.ArgumentParser(description='A股K线分析工具 - 新浪财经+Baostock')
    parser.add_argument('--code', required=True, help='股票代码 (如: 000001)')
    parser.add_argument('--period', default='daily', choices=['daily', 'weekly', 'monthly'],
                       help='周期: daily/weekly/monthly')
    parser.add_argument('--days', type=int, default=60, help='获取天数')
    parser.add_argument('--plot', action='store_true', help='生成K线图')
    parser.add_argument('--report', action='store_true', help='输出分析报告')
    parser.add_argument('--realtime', action='store_true', help='获取实时价格')
    parser.add_argument('--output', help='图表保存路径')
    parser.add_argument('--json', action='store_true', help='JSON格式输出')
    
    args = parser.parse_args()
    
    # 初始化数据源
    api = StockDataSource()
    
    # 获取实时价格
    realtime_data = None
    if args.realtime or args.report:
        print(f"正在获取 {args.code} 实时价格...")
        realtime_data = api.get_realtime_price(args.code)
        if realtime_data:
            print(f"✓ 实时价格: {realtime_data['price']:.2f} ({realtime_data['change_pct']:+.2f}%)")
        else:
            print("✗ 获取实时价格失败")
    
    # 获取K线数据
    print(f"正在获取 {args.code} {args.period}K线数据 ({args.days}天)...")
    df = api.get_kline_data(args.code, args.period, args.days)
    
    if df is None or df.empty:
        print("✗ 获取K线数据失败")
        sys.exit(1)
    
    print(f"✓ 成功获取 {len(df)} 条K线数据")
    
    # 计算技术指标
    df = calculate_ma(df)
    df = calculate_macd(df)
    df = calculate_rsi(df)
    df = calculate_bollinger(df)
    
    # 识别形态
    patterns = identify_patterns(df)
    
    # 输出结果
    if args.json:
        result = {
            'code': args.code,
            'name': realtime_data.get('name', '') if realtime_data else '',
            'realtime': realtime_data,
            'data': df.to_dict('records'),
            'patterns': patterns,
            'latest_indicators': {
                'close': float(df.iloc[-1]['close']),
                'ma5': float(df.iloc[-1]['MA5']) if 'MA5' in df.columns else None,
                'ma20': float(df.iloc[-1]['MA20']) if 'MA20' in df.columns else None,
                'rsi': float(df.iloc[-1]['RSI']) if 'RSI' in df.columns else None,
                'macd': float(df.iloc[-1]['MACD']) if 'MACD' in df.columns else None,
            }
        }
        print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
    
    if args.report:
        print(generate_report(df, patterns, realtime_data, args.code))
    
    if args.plot:
        stock_name = realtime_data.get('name', '') if realtime_data else ''
        plot_kline(df, args.code, stock_name, args.output)
    
    if not args.json and not args.report and not args.plot:
        latest = df.iloc[-1]
        print(f"\n{'='*40}")
        print(f"股票: {args.code} {realtime_data.get('name', '') if realtime_data else ''}")
        print(f"{'='*40}")
        print(f"最新: {realtime_data['price'] if realtime_data else latest['close']:.2f}")
        print(f"涨跌: {realtime_data['change_pct'] if realtime_data else latest['change_pct']:+.2f}%")
        print(f"开盘: {latest['open']:.2f}")
        print(f"最高: {latest['high']:.2f}")
        print(f"最低: {latest['low']:.2f}")
        if 'MA5' in df.columns:
            print(f"MA5:  {latest['MA5']:.2f}")
        if 'MA20' in df.columns:
            print(f"MA20: {latest['MA20']:.2f}")
        if 'RSI' in df.columns:
            print(f"RSI:  {latest['RSI']:.2f}")


if __name__ == '__main__':
    main()

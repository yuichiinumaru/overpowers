import { type ColorsTheme, Theme } from './theme.js';

const vaporwaveColors: ColorsTheme = {
  type: 'dark',
  Background: '#2d1b69',
  Foreground: '#ff69b4',
  LightBlue: '#87ceeb',
  AccentBlue: '#4169e1',
  AccentPurple: '#da70d6',
  AccentCyan: '#00ffff',
  AccentGreen: '#98fb98',
  AccentYellow: '#ffd700',
  AccentRed: '#ff1493',
  Comment: '#9370db',
  Gray: '#483d8b',
  GradientColors: ['#ff69b4', '#da70d6', '#00ffff'],



const vaporwaveSemanticColors = {
  text: {
    primary: vaporwaveColors.Foreground,
    secondary: vaporwaveColors.Gray,
    link: vaporwaveColors.AccentBlue,
    accent: vaporwaveColors.AccentPurple,
  },
  background: {
    primary: vaporwaveColors.Background,
    diff: {
      added: vaporwaveColors.DiffAdded,
      removed: vaporwaveColors.DiffRemoved,
    },
  },
  border: {
    default: vaporwaveColors.Gray,
    focused: vaporwaveColors.AccentBlue,
  },
  ui: {
    comment: vaporwaveColors.Comment,
    symbol: vaporwaveColors.Gray,
    gradient: vaporwaveColors.GradientColors,
  },
  status: {
    error: vaporwaveColors.AccentRed,
    success: vaporwaveColors.AccentGreen,
    warning: vaporwaveColors.AccentYellow,
  },
};

export const Vaporwave: Theme = new Theme('Vaporwave', 'dark', {
  hljs: { display: 'block', overflowX: 'auto', padding: '0.5em', background: vaporwaveColors.Background, color: vaporwaveColors.Foreground },
  'hljs-keyword': { color: vaporwaveColors.AccentPurple, fontWeight: 'bold' },
  'hljs-string': { color: vaporwaveColors.AccentCyan },
  'hljs-comment': { color: vaporwaveColors.Comment },
  'hljs-number': { color: vaporwaveColors.AccentYellow },
  'hljs-function': { color: vaporwaveColors.Foreground, fontWeight: 'bold' },
  'hljs-variable': { color: vaporwaveColors.LightBlue },
  'hljs-title': { color: vaporwaveColors.AccentPurple, fontWeight: 'bold' },
  'hljs-type': { color: vaporwaveColors.AccentCyan },
  'hljs-built_in': { color: vaporwaveColors.AccentRed },
}, vaporwaveColors,
  vaporwaveSemanticColors
);

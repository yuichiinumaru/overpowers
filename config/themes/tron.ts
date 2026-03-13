import { type ColorsTheme, Theme } from './theme.js';

const tronColors: ColorsTheme = {
  type: 'dark',
  Background: '#000000',
  Foreground: '#00ffff',
  LightBlue: '#40ccff',
  AccentBlue: '#00ffff',
  AccentPurple: '#0080ff',
  AccentCyan: '#00ffff',
  AccentGreen: '#00ff99',
  AccentYellow: '#ffff00',
  AccentRed: '#ff6600',
  Comment: '#004444',
  Gray: '#333333',
  GradientColors: ['#00ffff', '#ff6600', '#0080ff'],



const tronSemanticColors = {
  text: {
    primary: tronColors.Foreground,
    secondary: tronColors.Gray,
    link: tronColors.AccentBlue,
    accent: tronColors.AccentPurple,
  },
  background: {
    primary: tronColors.Background,
    diff: {
      added: tronColors.DiffAdded,
      removed: tronColors.DiffRemoved,
    },
  },
  border: {
    default: tronColors.Gray,
    focused: tronColors.AccentBlue,
  },
  ui: {
    comment: tronColors.Comment,
    symbol: tronColors.Gray,
    gradient: tronColors.GradientColors,
  },
  status: {
    error: tronColors.AccentRed,
    success: tronColors.AccentGreen,
    warning: tronColors.AccentYellow,
  },
};

export const Tron: Theme = new Theme('Tron', 'dark', {
  hljs: { display: 'block', overflowX: 'auto', padding: '0.5em', background: tronColors.Background, color: tronColors.Foreground },
  'hljs-keyword': { color: tronColors.AccentBlue, fontWeight: 'bold' },
  'hljs-string': { color: tronColors.AccentRed },
  'hljs-comment': { color: tronColors.Comment },
  'hljs-number': { color: tronColors.AccentYellow },
  'hljs-function': { color: tronColors.AccentBlue, fontWeight: 'bold' },
  'hljs-variable': { color: tronColors.LightBlue },
  'hljs-title': { color: tronColors.AccentRed, fontWeight: 'bold' },
  'hljs-type': { color: tronColors.AccentCyan },
  'hljs-built_in': { color: tronColors.AccentBlue },
}, tronColors,
  tronSemanticColors
);

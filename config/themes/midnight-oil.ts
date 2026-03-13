import { type ColorsTheme, Theme } from './theme.js';

const midnightOilColors: ColorsTheme = {
  type: 'dark',
  Background: '#1e2a3a',
  Foreground: '#f5f5dc',
  LightBlue: '#4682b4',
  AccentBlue: '#6495ed',
  AccentPurple: '#9370db',
  AccentCyan: '#20b2aa',
  AccentGreen: '#90ee90',
  AccentYellow: '#ffd700',
  AccentRed: '#cd5c5c',
  Comment: '#708090',
  Gray: '#2f4f4f',
  GradientColors: ['#1e2a3a', '#4682b4', '#f5f5dc'],



const midnightoilSemanticColors = {
  text: {
    primary: midnightoilColors.Foreground,
    secondary: midnightoilColors.Gray,
    link: midnightoilColors.AccentBlue,
    accent: midnightoilColors.AccentPurple,
  },
  background: {
    primary: midnightoilColors.Background,
    diff: {
      added: midnightoilColors.DiffAdded,
      removed: midnightoilColors.DiffRemoved,
    },
  },
  border: {
    default: midnightoilColors.Gray,
    focused: midnightoilColors.AccentBlue,
  },
  ui: {
    comment: midnightoilColors.Comment,
    symbol: midnightoilColors.Gray,
    gradient: midnightoilColors.GradientColors,
  },
  status: {
    error: midnightoilColors.AccentRed,
    success: midnightoilColors.AccentGreen,
    warning: midnightoilColors.AccentYellow,
  },
};

export const MidnightOil: Theme = new Theme('Midnight Oil', 'dark', {
  hljs: { display: 'block', overflowX: 'auto', padding: '0.5em', background: midnightOilColors.Background, color: midnightOilColors.Foreground },
  'hljs-keyword': { color: midnightOilColors.AccentBlue, fontWeight: 'bold' },
  'hljs-string': { color: midnightOilColors.AccentGreen },
  'hljs-comment': { color: midnightOilColors.Comment },
  'hljs-number': { color: midnightOilColors.AccentYellow },
  'hljs-function': { color: midnightOilColors.AccentPurple, fontWeight: 'bold' },
  'hljs-variable': { color: midnightOilColors.LightBlue },
  'hljs-title': { color: midnightOilColors.AccentCyan, fontWeight: 'bold' },
  'hljs-type': { color: midnightOilColors.AccentBlue },
  'hljs-built_in': { color: midnightOilColors.AccentYellow },
}, midnightOilColors,
  midnightoilSemanticColors
);

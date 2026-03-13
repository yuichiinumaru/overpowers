import { type ColorsTheme, Theme } from './theme.js';

const pastelKawaiiColors: ColorsTheme = {
  type: 'light',
  Background: '#fff0f5',
  Foreground: '#ff69b4',
  LightBlue: '#87ceeb',
  AccentBlue: '#dda0dd',
  AccentPurple: '#dda0dd',
  AccentCyan: '#afeeee',
  AccentGreen: '#98fb98',
  AccentYellow: '#fff8dc',
  AccentRed: '#ffb6c1',
  Comment: '#d8bfd8',
  Gray: '#f0e68c',
  GradientColors: ['#ffb6c1', '#dda0dd', '#87ceeb'],



const pastelkawaiiSemanticColors = {
  text: {
    primary: pastelkawaiiColors.Foreground,
    secondary: pastelkawaiiColors.Gray,
    link: pastelkawaiiColors.AccentBlue,
    accent: pastelkawaiiColors.AccentPurple,
  },
  background: {
    primary: pastelkawaiiColors.Background,
    diff: {
      added: pastelkawaiiColors.DiffAdded,
      removed: pastelkawaiiColors.DiffRemoved,
    },
  },
  border: {
    default: pastelkawaiiColors.Gray,
    focused: pastelkawaiiColors.AccentBlue,
  },
  ui: {
    comment: pastelkawaiiColors.Comment,
    symbol: pastelkawaiiColors.Gray,
    gradient: pastelkawaiiColors.GradientColors,
  },
  status: {
    error: pastelkawaiiColors.AccentRed,
    success: pastelkawaiiColors.AccentGreen,
    warning: pastelkawaiiColors.AccentYellow,
  },
};

export const PastelKawaii: Theme = new Theme('Pastel Kawaii', 'light', {
  hljs: { display: 'block', overflowX: 'auto', padding: '0.5em', background: pastelKawaiiColors.Background, color: pastelKawaiiColors.Foreground },
  'hljs-keyword': { color: pastelKawaiiColors.AccentPurple, fontWeight: 'bold' },
  'hljs-string': { color: pastelKawaiiColors.AccentGreen },
  'hljs-comment': { color: pastelKawaiiColors.Comment },
  'hljs-number': { color: pastelKawaiiColors.AccentBlue },
  'hljs-function': { color: pastelKawaiiColors.Foreground, fontWeight: 'bold' },
  'hljs-variable': { color: pastelKawaiiColors.LightBlue },
  'hljs-title': { color: pastelKawaiiColors.AccentRed, fontWeight: 'bold' },
  'hljs-type': { color: pastelKawaiiColors.AccentPurple },
  'hljs-built_in': { color: pastelKawaiiColors.AccentCyan },
}, pastelKawaiiColors,
  pastelkawaiiSemanticColors
);

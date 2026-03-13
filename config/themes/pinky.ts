import { type ColorsTheme, Theme } from './theme.js';

const pinkyColors: ColorsTheme = {
  type: 'dark',
  Background: '#2a0f1f',
  Foreground: '#ffb3d9',
  LightBlue: '#87ceeb',
  AccentBlue: '#4169e1',
  AccentPurple: '#da70d6',
  AccentCyan: '#ff69b4',
  AccentGreen: '#98fb98',
  AccentYellow: '#ffd700',
  AccentRed: '#ff1493',
  Comment: '#c5539f',
  Gray: '#696969',
  GradientColors: ['#ff1493', '#ff69b4', '#ffb3d9'],



const pinkySemanticColors = {
  text: {
    primary: pinkyColors.Foreground,
    secondary: pinkyColors.Gray,
    link: pinkyColors.AccentBlue,
    accent: pinkyColors.AccentPurple,
  },
  background: {
    primary: pinkyColors.Background,
    diff: {
      added: pinkyColors.DiffAdded,
      removed: pinkyColors.DiffRemoved,
    },
  },
  border: {
    default: pinkyColors.Gray,
    focused: pinkyColors.AccentBlue,
  },
  ui: {
    comment: pinkyColors.Comment,
    symbol: pinkyColors.Gray,
    gradient: pinkyColors.GradientColors,
  },
  status: {
    error: pinkyColors.AccentRed,
    success: pinkyColors.AccentGreen,
    warning: pinkyColors.AccentYellow,
  },
};

export const Pinky: Theme = new Theme(
  'Pinky',
  'dark',
  {
    hljs: {
      display: 'block',
      overflowX: 'auto',
      padding: '0.5em',
      background: pinkyColors.Background,
      color: pinkyColors.Foreground,
    },
    'hljs-keyword': {
      color: pinkyColors.AccentRed,
      fontWeight: 'bold',
    },
    'hljs-string': {
      color: pinkyColors.AccentGreen,
    },
    'hljs-comment': {
      color: pinkyColors.Comment,
    },
    'hljs-number': {
      color: pinkyColors.AccentYellow,
    },
    'hljs-function': {
      color: pinkyColors.AccentCyan,
      fontWeight: 'bold',
    },
    'hljs-variable': {
      color: pinkyColors.Foreground,
    },
    'hljs-title': {
      color: pinkyColors.AccentPurple,
      fontWeight: 'bold',
    },
    'hljs-type': {
      color: pinkyColors.LightBlue,
    },
    'hljs-built_in': {
      color: pinkyColors.AccentCyan,
    },
  },
  pinkyColors,
);

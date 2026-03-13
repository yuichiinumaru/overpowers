import { type ColorsTheme, Theme } from './theme.js';

const matrixColors: ColorsTheme = {
  type: 'dark',
  Background: '#000000',
  Foreground: '#00ff00',
  LightBlue: '#00ff41',
  AccentBlue: '#008800',
  AccentPurple: '#00cc00',
  AccentCyan: '#00ff41',
  AccentGreen: '#00ff00',
  AccentYellow: '#ffff00',
  AccentRed: '#ff0000',
  DiffAdded: '#004400',
  DiffRemoved: '#440000',
  Comment: '#004400',
  Gray: '#333333',
  GradientColors: ['#00ff00', '#00ff41', '#00cc00'],
};

const matrixSemanticColors = {
  text: {
    primary: matrixColors.Foreground,
    secondary: matrixColors.Gray,
    link: matrixColors.AccentBlue,
    accent: matrixColors.AccentPurple,
  },
  background: {
    primary: matrixColors.Background,
    diff: {
      added: matrixColors.DiffAdded,
      removed: matrixColors.DiffRemoved,
    },
  },
  border: {
    default: matrixColors.Gray,
    focused: matrixColors.AccentBlue,
  },
  ui: {
    comment: matrixColors.Comment,
    symbol: matrixColors.Gray,
    gradient: matrixColors.GradientColors,
  },
  status: {
    error: matrixColors.AccentRed,
    success: matrixColors.AccentGreen,
    warning: matrixColors.AccentYellow,
  },
};

export const Matrix: Theme = new Theme(
  'Matrix',
  'dark',
  {
    hljs: {
      display: 'block',
      overflowX: 'auto',
      padding: '0.5em',
      background: matrixColors.Background,
      color: matrixColors.Foreground,
    },
    'hljs-keyword': {
      color: matrixColors.AccentGreen,
      fontWeight: 'bold',
    },
    'hljs-string': {
      color: matrixColors.AccentCyan,
    },
    'hljs-comment': {
      color: matrixColors.Comment,
    },
    'hljs-number': {
      color: matrixColors.LightBlue,
    },
    'hljs-function': {
      color: matrixColors.AccentGreen,
      fontWeight: 'bold',
    },
    'hljs-variable': {
      color: matrixColors.Foreground,
    },
    'hljs-title': {
      color: matrixColors.AccentCyan,
      fontWeight: 'bold',
    },
    'hljs-type': {
      color: matrixColors.AccentBlue,
    },
    'hljs-built_in': {
      color: matrixColors.AccentGreen,
    },
  },
  matrixColors,
  matrixSemanticColors,
);

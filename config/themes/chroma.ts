import { type ColorsTheme, Theme } from './theme.js';

const chromaColors: ColorsTheme = {
  type: 'light',
  Background: '#fafafa',
  Foreground: '#2e2e2e',
  LightBlue: '#1976d2',
  AccentBlue: '#2196f3',
  AccentPurple: '#9c27b0',
  AccentCyan: '#00bcd4',
  AccentGreen: '#4caf50',
  AccentYellow: '#ff9800',
  AccentRed: '#f44336',
  Comment: '#9e9e9e',
  Gray: '#757575',
  GradientColors: ['#f44336', '#ff9800', '#4caf50'],



const chromaSemanticColors = {
  text: {
    primary: chromaColors.Foreground,
    secondary: chromaColors.Gray,
    link: chromaColors.AccentBlue,
    accent: chromaColors.AccentPurple,
  },
  background: {
    primary: chromaColors.Background,
    diff: {
      added: chromaColors.DiffAdded,
      removed: chromaColors.DiffRemoved,
    },
  },
  border: {
    default: chromaColors.Gray,
    focused: chromaColors.AccentBlue,
  },
  ui: {
    comment: chromaColors.Comment,
    symbol: chromaColors.Gray,
    gradient: chromaColors.GradientColors,
  },
  status: {
    error: chromaColors.AccentRed,
    success: chromaColors.AccentGreen,
    warning: chromaColors.AccentYellow,
  },
};

export const Chroma: Theme = new Theme(
  'Chroma',
  'light',
  {
    hljs: {
      display: 'block',
      overflowX: 'auto',
      padding: '0.5em',
      background: chromaColors.Background,
      color: chromaColors.Foreground,
    },
    'hljs-keyword': {
      color: chromaColors.AccentBlue,
      fontWeight: 'bold',
    },
    'hljs-string': {
      color: chromaColors.AccentGreen,
    },
    'hljs-comment': {
      color: chromaColors.Comment,
    },
    'hljs-number': {
      color: chromaColors.AccentYellow,
    },
    'hljs-function': {
      color: chromaColors.AccentRed,
      fontWeight: 'bold',
    },
    'hljs-variable': {
      color: chromaColors.Foreground,
    },
    'hljs-title': {
      color: chromaColors.AccentPurple,
      fontWeight: 'bold',
    },
    'hljs-type': {
      color: chromaColors.AccentCyan,
    },
    'hljs-built_in': {
      color: chromaColors.LightBlue,
    },
  },
  chromaColors,
);

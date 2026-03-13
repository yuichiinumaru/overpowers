import { type ColorsTheme, Theme } from './theme.js';

const odysseyColors: ColorsTheme = {
  type: 'dark',
  Background: '#0d1117',
  Foreground: '#c9d1d9',
  LightBlue: '#58a6ff',
  AccentBlue: '#1f6feb',
  AccentPurple: '#bc8cff',
  AccentCyan: '#56d4dd',
  AccentGreen: '#7ee787',
  AccentYellow: '#f2cc60',
  AccentRed: '#ff7b72',
  Comment: '#8b949e',
  Gray: '#484f58',
  GradientColors: ['#58a6ff', '#bc8cff', '#56d4dd'],



const odysseySemanticColors = {
  text: {
    primary: odysseyColors.Foreground,
    secondary: odysseyColors.Gray,
    link: odysseyColors.AccentBlue,
    accent: odysseyColors.AccentPurple,
  },
  background: {
    primary: odysseyColors.Background,
    diff: {
      added: odysseyColors.DiffAdded,
      removed: odysseyColors.DiffRemoved,
    },
  },
  border: {
    default: odysseyColors.Gray,
    focused: odysseyColors.AccentBlue,
  },
  ui: {
    comment: odysseyColors.Comment,
    symbol: odysseyColors.Gray,
    gradient: odysseyColors.GradientColors,
  },
  status: {
    error: odysseyColors.AccentRed,
    success: odysseyColors.AccentGreen,
    warning: odysseyColors.AccentYellow,
  },
};

export const Odyssey: Theme = new Theme(
  'Odyssey',
  'dark',
  {
    hljs: {
      display: 'block',
      overflowX: 'auto',
      padding: '0.5em',
      background: odysseyColors.Background,
      color: odysseyColors.Foreground,
    },
    'hljs-keyword': {
      color: odysseyColors.AccentBlue,
      fontWeight: 'bold',
    },
    'hljs-string': {
      color: odysseyColors.AccentGreen,
    },
    'hljs-comment': {
      color: odysseyColors.Comment,
    },
    'hljs-number': {
      color: odysseyColors.AccentYellow,
    },
    'hljs-function': {
      color: odysseyColors.LightBlue,
      fontWeight: 'bold',
    },
    'hljs-variable': {
      color: odysseyColors.Foreground,
    },
    'hljs-title': {
      color: odysseyColors.AccentCyan,
      fontWeight: 'bold',
    },
    'hljs-type': {
      color: odysseyColors.AccentPurple,
    },
    'hljs-built_in': {
      color: odysseyColors.LightBlue,
    },
  },
  odysseyColors,
);

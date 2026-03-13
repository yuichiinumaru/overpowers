import { type ColorsTheme, Theme } from './theme.js';

const sakuraColors: ColorsTheme = {
  type: 'dark',
  Background: '#1a0f16',
  Foreground: '#f0d0d0',
  LightBlue: '#9bb7ff',
  AccentBlue: '#7b9eff',
  AccentPurple: '#d197d9',
  AccentCyan: '#a4d3e8',
  AccentGreen: '#b8d4a0',
  AccentYellow: '#f4d794',
  AccentRed: '#ff9bb5',
  Comment: '#8d5a75',
  Gray: '#4a3a42',
  GradientColors: ['#ff9bb5', '#d197d9', '#f0d0d0'],



const sakuraSemanticColors = {
  text: {
    primary: sakuraColors.Foreground,
    secondary: sakuraColors.Gray,
    link: sakuraColors.AccentBlue,
    accent: sakuraColors.AccentPurple,
  },
  background: {
    primary: sakuraColors.Background,
    diff: {
      added: sakuraColors.DiffAdded,
      removed: sakuraColors.DiffRemoved,
    },
  },
  border: {
    default: sakuraColors.Gray,
    focused: sakuraColors.AccentBlue,
  },
  ui: {
    comment: sakuraColors.Comment,
    symbol: sakuraColors.Gray,
    gradient: sakuraColors.GradientColors,
  },
  status: {
    error: sakuraColors.AccentRed,
    success: sakuraColors.AccentGreen,
    warning: sakuraColors.AccentYellow,
  },
};

export const Sakura: Theme = new Theme(
  'Sakura',
  'dark',
  {
    hljs: {
      display: 'block',
      overflowX: 'auto',
      padding: '0.5em',
      background: sakuraColors.Background,
      color: sakuraColors.Foreground,
    },
    'hljs-keyword': {
      color: sakuraColors.AccentRed,
      fontWeight: 'bold',
    },
    'hljs-string': {
      color: sakuraColors.AccentGreen,
    },
    'hljs-comment': {
      color: sakuraColors.Comment,
    },
    'hljs-number': {
      color: sakuraColors.AccentYellow,
    },
    'hljs-function': {
      color: sakuraColors.AccentPurple,
      fontWeight: 'bold',
    },
    'hljs-variable': {
      color: sakuraColors.Foreground,
    },
    'hljs-title': {
      color: sakuraColors.AccentCyan,
      fontWeight: 'bold',
    },
    'hljs-type': {
      color: sakuraColors.LightBlue,
    },
    'hljs-built_in': {
      color: sakuraColors.AccentPurple,
    },
  },
  sakuraColors,
);

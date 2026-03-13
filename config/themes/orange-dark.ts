import { type ColorsTheme, Theme } from './theme.js';

const orangeDarkColors: ColorsTheme = {
  type: 'dark',
  Background: '#1a0f0a',
  Foreground: '#ffcc80',
  LightBlue: '#64b5f6',
  AccentBlue: '#42a5f5',
  AccentPurple: '#ba68c8',
  AccentCyan: '#4dd0e1',
  AccentGreen: '#66bb6a',
  AccentYellow: '#ffc107',
  AccentRed: '#ff7043',
  Comment: '#8d6e63',
  Gray: '#5d4037',
  GradientColors: ['#ff7043', '#ffcc80', '#ffc107'],



const orangedarkSemanticColors = {
  text: {
    primary: orangedarkColors.Foreground,
    secondary: orangedarkColors.Gray,
    link: orangedarkColors.AccentBlue,
    accent: orangedarkColors.AccentPurple,
  },
  background: {
    primary: orangedarkColors.Background,
    diff: {
      added: orangedarkColors.DiffAdded,
      removed: orangedarkColors.DiffRemoved,
    },
  },
  border: {
    default: orangedarkColors.Gray,
    focused: orangedarkColors.AccentBlue,
  },
  ui: {
    comment: orangedarkColors.Comment,
    symbol: orangedarkColors.Gray,
    gradient: orangedarkColors.GradientColors,
  },
  status: {
    error: orangedarkColors.AccentRed,
    success: orangedarkColors.AccentGreen,
    warning: orangedarkColors.AccentYellow,
  },
};

export const OrangeDark: Theme = new Theme(
  'OrangeDark',
  'dark',
  {
    hljs: {
      display: 'block',
      overflowX: 'auto',
      padding: '0.5em',
      background: orangeDarkColors.Background,
      color: orangeDarkColors.Foreground,
    },
    'hljs-keyword': {
      color: orangeDarkColors.AccentRed,
      fontWeight: 'bold',
    },
    'hljs-string': {
      color: orangeDarkColors.AccentGreen,
    },
    'hljs-comment': {
      color: orangeDarkColors.Comment,
    },
    'hljs-number': {
      color: orangeDarkColors.AccentYellow,
    },
    'hljs-function': {
      color: '#ff8a65',
      fontWeight: 'bold',
    },
    'hljs-variable': {
      color: orangeDarkColors.Foreground,
    },
    'hljs-title': {
      color: orangeDarkColors.AccentCyan,
      fontWeight: 'bold',
    },
    'hljs-type': {
      color: orangeDarkColors.AccentPurple,
    },
    'hljs-built_in': {
      color: orangeDarkColors.AccentBlue,
    },
  },
  orangeDarkColors,
);

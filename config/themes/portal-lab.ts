import { type ColorsTheme, Theme } from './theme.js';

const portalLabColors: ColorsTheme = {
  type: 'light',
  Background: '#f8f8ff',
  Foreground: '#2f4f4f',
  LightBlue: '#87cefa',
  AccentBlue: '#0080ff',
  AccentPurple: '#4682b4',
  AccentCyan: '#00bfff',
  AccentGreen: '#32cd32',
  AccentYellow: '#ffa500',
  AccentRed: '#ff6347',
  Comment: '#708090',
  Gray: '#d3d3d3',
  GradientColors: ['#f8f8ff', '#0080ff', '#ffa500'],



const portallabSemanticColors = {
  text: {
    primary: portallabColors.Foreground,
    secondary: portallabColors.Gray,
    link: portallabColors.AccentBlue,
    accent: portallabColors.AccentPurple,
  },
  background: {
    primary: portallabColors.Background,
    diff: {
      added: portallabColors.DiffAdded,
      removed: portallabColors.DiffRemoved,
    },
  },
  border: {
    default: portallabColors.Gray,
    focused: portallabColors.AccentBlue,
  },
  ui: {
    comment: portallabColors.Comment,
    symbol: portallabColors.Gray,
    gradient: portallabColors.GradientColors,
  },
  status: {
    error: portallabColors.AccentRed,
    success: portallabColors.AccentGreen,
    warning: portallabColors.AccentYellow,
  },
};

export const PortalLab: Theme = new Theme('Portal Lab', 'light', {
  hljs: { display: 'block', overflowX: 'auto', padding: '0.5em', background: portalLabColors.Background, color: portalLabColors.Foreground },
  'hljs-keyword': { color: portalLabColors.AccentBlue, fontWeight: 'bold' },
  'hljs-string': { color: portalLabColors.AccentGreen },
  'hljs-comment': { color: portalLabColors.Comment },
  'hljs-number': { color: portalLabColors.AccentYellow },
  'hljs-function': { color: portalLabColors.AccentBlue, fontWeight: 'bold' },
  'hljs-variable': { color: portalLabColors.AccentPurple },
  'hljs-title': { color: portalLabColors.AccentRed, fontWeight: 'bold' },
  'hljs-type': { color: portalLabColors.AccentCyan },
  'hljs-built_in': { color: portalLabColors.AccentBlue },
}, portalLabColors,
  portallabSemanticColors
);

import { extendTheme } from "@chakra-ui/react";
import defaultTheme from "@chakra-ui/theme";

export const theme = extendTheme({
  fonts: {
    heading: `'Inter', sans-serif`,
    body: `'Inter', sans-serif`,
  },
  colors: {
    app: {
      primary: "#3D5A80",
      secondary: "#EE6C4D",
    },
  },
});

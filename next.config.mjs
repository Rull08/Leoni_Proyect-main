/** @type {import('next').NextConfig} */
const nextConfig = {
    experimental: {
        turbo: {
          rules: {
            '*.svg': {
              loaders: ['@svgr/webpack'],
              as: '*.js',
            },
          },
        },
    },
    webpack: (config) => {
      config.resolve.fallback = {
        fs: false,
        path: false,
        os: false,
        esbuild: false,
      };
      return config;
    },
  };
  
  export default nextConfig;
  
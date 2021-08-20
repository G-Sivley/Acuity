# Building

Requirements
```
node - >=v10
npm

Run all commands from the client/ directory unless specified otherwise
```

## Installing Dependencies
- `npm install`
Installs the node_modules, react, webpack etc..

### Building
- `npm run build`
Resolves all scripts from public/index.html, transpiles using babel ( jsx -> js, esm -> cjs ), and then bundles it for the browser

### Hot Reload
- `npm start`
Starts a webpack server with 'HOT RELOAD' ( Changes in JS/CSS files are reflected in webpage without reloading )
set the HOT_RELOAD env variable to true in .flaskenv for this to work correctly

To use the normal build just unset the HOT_RELOAD variable

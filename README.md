# logeo

## Deployment

To run this project run this in the console

```bash
  cd logeo

  py manage.py makemigrations

  py manage.py migrate
```
## Then
```bash
  npx webpack --config webpack.config.js --watch --mode 'production'
```
## And Then
```bash
  py manage.py runserver
```


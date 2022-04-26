# GoogleTool
Tools for Google's Service

## Environment
```bash
conda create --name googletool python=3.8 -y
```
```bash
python -m ipykernel install --user --name googletool --display-name "GoogleTool"
```

## Google Drive
- [Guiding Doc](https://developers.google.com/drive/api/guides/about-sdk)
- [API Reference](https://developers.google.com/drive/api/v3/reference/files)
- [Scope Documentation](https://developers.google.com/identity/protocols/oauth2/scopes#drive)
```bash
https://www.googleapis.com/auth/drive
```

## Google Sheet
- [API Reference](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/get#body.QUERY_PARAMETERS.ranges)
- [Scope Documentation](https://developers.google.com/sheets/api/guides/authorizing#OAuth2Authorizing)
```bash
https://www.googleapis.com/auth/spreadsheets
```

# Fitly

Just another URL Shortener service. Fitly was written on Flask and Vue JS. Postgresql was used as db.

### Requirements
- `docker ^18.09.05`
- `docker-compose ^1.23.1`

## Development
```sh
docker-compose -f docker-compose.dev.yml up 
```

Configuration stores in `.env.dev`

## Production
```sh
docker-compose -f docker-compose.prod.yml up 
```

Configuration stores in `.env.prod`



## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
Inspired by [bitly.com](https://bitly.com/)

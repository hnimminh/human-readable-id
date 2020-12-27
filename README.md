<p  align="center">
  <strong>HRID: Human Readable Identifier</strong>
  <br>
  <code>The Human Readable ID Generator Library For Python3</code>
  <br>
</p>

## Usage

Install
```
pip3 install hrid
```

Use in Python code
```python
from hrid import HRID

hruuid = HRID()
uuid = hruuid.generate()
print(uuid)
```

## Credit
* [Dictionary Source] (https://github.com/dariusk/corpora)
* [Influenced by Google API design] (https://cloud.google.com/blog/products/gcp/api-design-choosing-between-names-and-identifiers-in-urls)

## License

[MIT](./LICENSE)
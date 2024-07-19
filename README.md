# isRed
----
isRed is a toy Redis clone capable of handling
basic commands like `PING`, `SET` and `GET`, reading RDB files, and more. 

**Note**: [These](https://codecrafters.io) are the resources I used to build isRed.



## Give it a try!

1. Ensure you have `python (3.x)` installed locally
1. Run `./your_program.sh` to run your Redis server, which is implemented in
   `app/main.py`.

## Troubleshooting

#### module `socket` has no attribute `create_server`

When running your server locally, you might see an error like this:

```
Traceback (most recent call last):
  File "/.../python3.7/runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "/.../python3.7/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/app/app/main.py", line 11, in <module>
    main()
  File "/app/app/main.py", line 6, in main
    s = socket.create_server(("localhost", 6379), reuse_port=True)
AttributeError: module 'socket' has no attribute 'create_server'
```

This is because `socket.create_server` was introduced in Python 3.8, and you
might be running an older version.

You can fix this by installing Python 3.8 locally and using that.

If you'd like to use a different version of Python, change the `language_pack`
value in `codecrafters.yml`.

bind = "0.0.0.0:8000"  # Host and port to bind to (0.0.0.0 makes it accessible from all network interfaces)
workers = 8           # Number of worker processes (adjust to your server's resources)
timeout = 500         # Maximum time, in seconds, a worker is allowed to run
threads = 4    # Number of threads per worker (set to 1 for single-threaded)
accesslog = "-"        # "-" means logs to stdout
errorlog = "-"         # "-" means logs to stdout


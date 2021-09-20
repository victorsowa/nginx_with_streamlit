# nginx_with_streamlit

## Purpose

Create an example where multiple streamlit applications are subdomains of an web-application.

## Running the example

To run the example first build the docker-compose with  ``docker-compose build`` then run it with ``docker-compose up``.

This will start two docker containers with streamlit applications on port 5001 and 5002 respectivly as well as a nginx docker container running on port 8080.

Go to http://localhost:8080 to see the built and running example. app1 should be available at http://localhost:8080/app1 and app2 should be available at http://localhost:8080/app2.

## Important points

- All streamlit static files are served from app1. This is because streamlit always looks for static files in `/static` and therefore it is not possible for several applications static files to be served. From this done with this statement in the nginx.conf:

    ```
        location ^~ /static {
            proxy_pass http://172.17.0.1:5001/static/;
        }
    ```

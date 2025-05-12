FROM httpd:latest

# Copy your custom HTML files into the container
COPY . /usr/local/apache2/htdocs/

# Expose port 80
EXPOSE 80


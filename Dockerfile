FROM httpd:2.4

# Copy your custom HTML files into the container
# Assuming you have an 'html/' folder with index.html and other assets
COPY . /usr/local/apache2/htdocs/

# Expose port 80
EXPOSE 80

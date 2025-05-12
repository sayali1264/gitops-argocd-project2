# Use the official httpd image from Docker Hub
FROM httpd:2.4

# Copy your custom HTML files into the container
# Assuming you have an 'html/' folder with index.html and other assets
COPY . /usr/local/apache2/htdocs/

# Expose port 80
EXPOSE 80

# The default command in httpd image is already to run Apache in the foreground

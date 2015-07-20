echo "Building PostGIS..."

cd

if [ ! -f postgis-2.0.5.tar.gz ]; then
    echo "No PostGIS installation, proceeding with build."
    wget http://download.osgeo.org/postgis/source/postgis-2.0.5.tar.gz
    tar xfz postgis-2.0.5.tar.gz
    cd postgis-2.0.5

    ./configure
    make

    make install
    ldconfig
    make comments-install

    ln -sf /usr/share/postgresql-common/pg_wrapper /usr/local/bin/shp2pgsql
    ln -sf /usr/share/postgresql-common/pg_wrapper /usr/local/bin/pgsql2shp
    ln -sf /usr/share/postgresql-common/pg_wrapper /usr/local/bin/raster2pgsql
    echo "Finished Build"
else
  echo "Found build, skipping"
fi


# Install libQt4 in ubuntu 20
sudo add-apt-repository ppa:rock-core/qt4

sudo apt-get update

sudo apt-get install libqt4-declarative qt4-dev-tools qt4-qmake libqtwebkit4

# Unistall
sudo add-apt-repository ppa:rock-core/qt4 -r -y

sudo apt remove libqt4* libqtcore4 libqtgui4 libqtwebkit4 qt4* --auto-remove

### Ref
https://www.edivaldobrito.com.br/como-instalar-as-bibliotecas-qt4-no-ubuntu-20-04-lts-e-derivados/

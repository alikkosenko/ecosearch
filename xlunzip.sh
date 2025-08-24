unzip -o Транзит\ Авто__.xlsx -d transit
rm Транзит\ Авто__.xlsx
cd transit/xl
scp -i "/home/alikk/Downloads/co.pem" media/* ubuntu@ec2-54-195-147-81.eu-west-1.compute.amazonaws.com:/home/ubuntu/Projects/ecosearch/static
scp -i "/home/alikk/Downloads/co.pem" drawings/drawing1.xml  ubuntu@ec2-54-195-147-81.eu-west-1.compute.amazonaws.com:/home/ubuntu/Projects/ecosearch/drawing1.xml

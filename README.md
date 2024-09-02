# Rag Implementation

 ## Setting up milvus in docker
  - Check if docker is downloaded, if not use `sudo snap install docker`
  - Create a dir{milvus-docker-setup} - `mkdir milvus-docker-setup`, then `milvus-docker-setup`
  - Create a Docker compose conf file for setting up milvus instance - `nvim docker-compose.yml`
  - Continuing the above -> etcd:
                                - Uses the coreos etcd image
                                - Setting enviornment cariables for etcd configuration
                                - mounting a docker vol'(`etcd_data`) to store any data written to `etcd-data` inside the container
                                - connects to a docker network (`milvus-network`)
  - milvus:
        - mapping port `19530` on the host to port `19530` on the container
        - running milvus in standalone mode with the command `milvus rum standalone`
        - mounts a docker vol'(`milvus_data`) to store data written to milvus 
        - connects to same docker net (`milvus-network`)
                            

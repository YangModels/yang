#!/bin/bash
#
# Prepare a models directory based on the protocol agent being run.
# NOTE: This script should be run in the same directory where it resides
# Example:
#
# ./prepare.sh [-h ] -a { netconf | gnmi | restconf }
#
#  creates a directory called {AGENT}_models under the models directory
#
#
# For netconf (default): ./prepare.sh 
#      Creates ./netconf_models
# 
# For restconf: ./prepare.sh -a restconf 
#      Creates ./restconf_models
#
# For gnmi: ./prepare.sh -a gnmi 
#      Creates ./gnmi_models
#
# All your models will be in the created models directory.
#
# ##########################################################




### USAGE
usage()
{
     echo ""
     echo "./prepare.sh [-h ] -a { netconf | gnmi | restconf }"
     echo ""
     echo " creates a directory called {AGENT}_models under the models directory"
     echo " "
     echo " "
     echo "For netconf (default): ./prepare.sh "
     echo "     Creates ./netconf_models"
     echo ""
     echo "For restconf: ./prepare.sh -a restconf "
     echo "     Creates ./restconf_models"
     echo "     "
     echo "For gnmi: ./prepare.sh -a gnmi "
     echo "     Creates ./gnmi_models"
     echo ""
     echo "All your models will be in the created models directory."
     echo ""

}


### Setup $1 = AGENT, $2 = DIRECTORY
setup()
{
    CP_YANG="cp -L *.yang $2/"
    CP_JSON="cp -L *.json $2/"
    CP_NETCONF="cp -L *.xml $2"
    CP_GNMI="cp -L extensions/*.yang $2/"
    echo "** Copying Model Files for $1 to ./${2}/"
    case $1 in
        netconf)
                            $CP_YANG ; $CP_JSON ; $CP_NETCONF
                            ;;
        restconf)
                            $CP_YANG ; $CP_JSON
                            ;;
        gnmi)
                            $CP_YANG ; $CP_JSON ; $CP_GNMI
                            ;;
        * )
                            echo "Error: Unsupported agent $1" && exit 1 
                            ;;
    esac
    echo "** Using pyang to verify all models in ./${2}/"
    echo "** EXEC: cd ./$2/"
    echo "** EXEC: ../check-models.sh"
    cd "$2"
    ../check-models.sh
}

AGENT=netconf

while [ "$1" != "" ]; do
    case $1 in
        -a | --agent )          shift
                                AGENT=$1
                                ;;
        -h | --help )           usage
                                exit
                                ;;
        * )                     usage
                                exit 1
    esac
    shift
done

if [[ "$AGENT" =~ "(netconf|restconf|gnmi)" ]]; then
    echo "Error: Invalid agent $AGENT must be one of netconf|restconf|gnmi."
    exit 1
fi


DIRECTORY="${AGENT}_models"

[ -d "$DIRECTORY" ] || mkdir "$DIRECTORY"

if [[ -d "$DIRECTORY" ]]; then
    setup "$AGENT" "$DIRECTORY"
else
    echo "Error: Failed to create directory $DIRECTORY"
    exit 1
fi


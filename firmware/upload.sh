# Used to upload firmware. Assumes device is plugged in and already
# has circuit py loaded

helpFunction()
{
   echo ""
   echo "Usage: $0 deviceName -a parameterA -b parameterB -c parameterC"
   echo -e "\t deviceName Name of the device, one of [bc,bp]"
   echo -e "\t -a Description of what is parameterA"
   echo -e "\t -b Description of what is parameterB"
   echo -e "\t -c Description of what is parameterC"
   exit 1 # Exit script after printing help
}

while getopts "a:b:c:" opt
do
   case "$opt" in
      a ) parameterA="$OPTARG" ;;
      b ) parameterB="$OPTARG" ;;
      c ) parameterC="$OPTARG" ;;
      ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done


# Copy over libraries
rsync -cr ./user_libs /Volumes/CIRCUITPY/lib

# Copy over main file

deviceName=$1

if [[ deviceName == "bc" ]]; then
  rsync -c ./beyblock20_controller/code.py /Volumes/CIRCUITPY/lib/code.py
elif [[ deviceName == "bp"]]; then
  rsync -c ./beyblock20_controller/code.py /Volumes/CIRCUITPY/lib/code.py
else
  helpFunction
fi

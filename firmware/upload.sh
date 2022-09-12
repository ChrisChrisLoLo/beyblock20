# Used to upload firmware. Assumes device is plugged in and already
# has circuit py loaded

helpFunction()
{
   echo ""
   echo "Usage: $0 deviceName -a parameterA -b parameterB -c parameterC"
   echo "\t deviceName Name of the device, one of [bc,bp]"
   echo "\t -a Description of what is parameterA"
   echo "\t -b Description of what is parameterB"
   echo "\t -c Description of what is parameterC"
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

# Copy over main file

deviceName=$1

if [[ $deviceName == "bc" ]]; then
  rsync -c ./beyblock20_controller/* /Volumes/CIRCUITPY/
elif [[ $deviceName == "bp" ]]; then
  rsync -c ./beyblock20_peripheral/* /Volumes/CIRCUITPY/
else
  helpFunction
fi

# Copy over libraries
rsync -cr ./libs/kmk_firmware/kmk /Volumes/CIRCUITPY/
rsync -cr ./libs/kmk_firmware/boot.py /Volumes/CIRCUITPY/boot.py
rsync -cr ./libs/user_libs /Volumes/CIRCUITPY/

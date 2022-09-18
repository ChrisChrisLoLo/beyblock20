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
  #driveName="           "
  #driveName="NO NAME"
  driveName="CIRCUITPY"
  # rsync -c ./beyblock20_controller/* /Volumes/CIRCUITPY/
  # # Copy over libraries
  # rsync -cr ./libs/kmk_firmware/kmk /Volumes/CIRCUITPY/
  # rsync -cr ./libs/kmk_firmware/boot.py /Volumes/CIRCUITPY/boot.py
  # rsync -cr ./libs/user_libs /Volumes/CIRCUITPY/
  # rsync -cr ./libs/adafruit* /Volumes/CIRCUITPY/

  rsync -c ./beyblock20_controller/* /Volumes/"$driveName"/
  # Copy over libraries
  rsync -cr ./libs/kmk_firmware/kmk /Volumes/"$driveName"/
  rsync -cr ./libs/kmk_firmware/boot.py /Volumes/"$driveName"/boot.py
  rsync -cr ./libs/user_libs /Volumes/"$driveName"/
  rsync -cr ./libs/adafruit* /Volumes/"$driveName"/
elif [[ $deviceName == "bp" ]]; then
  rsync -c ./beyblock20_peripheral/* /Volumes/CIRCUITPY/
elif [[ $deviceName == "kp" ]]; then
  rsync -c ./knoblin3_peripheral/* /Volumes/CIRCUITPY/
elif [[ $deviceName == "rst" ]]; then
  # file used to reset device
  openssl rand -base64 12 > /Volumes/CIRCUITPY/rst
else
  helpFunction
fi



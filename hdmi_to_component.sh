sudo sed -i 's/sdtv_mode=0/sdtv_mode=2/g' /boot/config.txt
sudo sed -i 's/#sdtv_mode=2/sdtv_mode=2/g' /boot/config.txt
sudo sed -i 's/hdmi_force_hotplug=1/#hdmi_force_hotplug=1/g' /boot/config.txt

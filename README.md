
# Codeforces Contest Announcer

I have always been into competitive programming into spend a good amount of time wandering around sites like codechef, leetcode and codeforces. I also try to give contests on these sites regularly, like Codechef conducts contest every Wednesday, Leetcode conducts contest every Saturdat and Sunday but Codeforces.... Contests on Codeforces are so random, that I have only ever given two contests.

In order to fix that issue, I have build this python script that will regulary find Codeforces contest and announce it using Alexa every day *if there is a contest available on that day* at your desired time.



## Installation

Clone the github repo using the command

```bash
git clone https://github.com/NotTheRightGuy/Codeforces-Announcer.git
```

Run the following commands to install necessary dependancies.

``` bash
cd Codeforces-Announcer
pip install -r requirements.txt
```


## Configuration

After installing dependancies you need to setup the neccesary keys required to run this script. Open `config.json` to find

```json
{
    "SUPABASE_KEY": "",
    "SUPABASE_URL": "",

    "VOICEMONKEY_API": "",

    "ALEXA_DEVICE_NAME": "",
    "ROUTINE_NAME": "",

    "DELETE_CONTEST_TIME": "00:00",
    "UPLOAD_TO_DATABASE_TIME": "06:00",
    "EVENT_TRIGGER_TIME": "07:30"
}

```

The project uses supabase in order to store the contests fetched from the codeforces API which are yet to happen. The contests will automatically get deleted from your table once the contest gets over. This action happens everyday at mentioned `DELETE_CONTEST_TIME` which you can change accordingly.

To get `SUPABASE_KEY` and `SUPABASE_URL` head over to [Supabase](https://supabase.com). Create a new project and give it whatever name you want. 

While the project is setting up you will find your SUPABASE_URL and SUPABASE_API. If the project is already setup, head over the project setting and you will find your URL and KEY here ![Supabase API Location](https://i.ibb.co/qWtM2N5/Supabase-URL.jpg)

### Voice Monkey
In order to connect with Alexa we uses API provided by [Voice Monkey](https://voicemonkey.io/). There is a paid as well as a **free** tier. The paid tier allows you to announce the time along side the announcement but if that is not your concern, free tier comes with everything you need using the Routine API.

Head over to [Voice Monkey](https://voicemonkey.io/) and *sign in with your amazon account which is connected with your Alexa Devices.*

Once signed in, Go to Settings > API Credientials and copy the API token and paste in `config.json` as value of `VOICEMONKEY_API`

**Voice Monkey provides 14 days of free trial where you can use the Announcement API, once the trial is over, simply restart the script with Routine API**

Now, head over to dashboard, click on manage devices and a new device in Speakers Section.
- Keep it as a single device
- ***Start the device name with 'VM' followed by whatever you want.***, For example if you want to name your device as *Contest*, name it as **VM Contest**. This allows Voice Monkey to recognise your device.

Once you are back to devices page, you will find the device-id of the newly added device. Add this to `config.json` as the value of `ALEXA_DEVICE_NAME`

Once we are done with adding the device, head over to **Devices**, scroll down a bit and you will find a section to add a new Routine Trigger just underneath the speaker section where you added the device.
- Add a new routine trigger
- Give it whatever name you want

Once you are back to devices page, you will find the device-id of the newly added routine. Add this to `config.json` as the value of `ROUTINE_NAME`



Once we are done with all this go to the **Alexa App** to create 2 new routines.

1. First Routine will be use to make announcement with dynamic content (for Announcement API)
2. Second Routine will be have static content and can be triggered using the script. (for Routine API, once trial is over)

## Setting up Routine for Announcement API
- Create a new Routine
- Name the routine whatever you want
- In **When this happens**
    - Select Smart Home
    - Select the name of the device starting with VM you created earlier
- In actions
    - Select Skills
    - Select Your Skills
    - Select **Voice Monkey - Smart Home + Routine Triggers..**
    (if this is not available, you may need to install the skill first)
- Select the device you want the announcement to be made from.


## Setting up Routine for Routine API
- Create a new routine 
- Name the routine whatever you want
- In **When this happens**
    - Select Smart Home
    - Select the name of trigger you created earlier on Voice Monkey
- In actions
    - Add Whatever you want to occur when this routine gets triggered
    - We will make alexa say "Contest Alert!, There is a contest scheduled for today"
- Select the device you want the announcement to be made from.

## Running the script
Once we are done with the setup run the program as
```bash
python main.py
```
OR
```bash
python3 main.py
```
OR
```bash
py main.py
```

Test if the script is working fine, but populating the database and selecting option 4 or 5. Your Alexa will respond, if there is a contest scheduled for that day.
## Issues

### Alexa is no longer making announcements.
It might be possible that your Voice Monkey Trial has expired and you are still using Announcement API. Make sure to restart the app and select Routine API once the trial is over or if you want to continue using Announcement API, please buy the premium tier of Voice Monkey.

***If there is any other issues which is not covered here, feel free to add a new issue and steps to recreate the issue with screenshot of issue.***

## Contributing

Contributions are always welcome! weather it's some changes to the documentation or you just managed to make my app 1500 times faster. Just create a new pull request and I will get back to you as soon as possible.



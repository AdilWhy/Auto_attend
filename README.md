## Auto attend script in wsp system
Automatically attend for a subject and send a message via telegram bot


### To run this script you need to follow these steps:

1. Install Docker https://docs.docker.com/engine/install/ubuntu/

2. Depending on your server configuration, use the appropriate command:
    - ARM: `docker compose up -d`
    - x86: `docker compose -f docker_compose_x86.yml up -d`

3. Change secrets in `configurations/settings.py` 

4. Run this command
```
nohup python3 attendv2.py &
```

*(Optional)* You can run this script automatically by     installing and customizing cron
<details>
    <summary>For Ubuntu</summary>

    sudo apt-get update
    sudo apt-get install cron
    echo "*/5 * * * * pgrep -f attend2.py | pgrep python || nohup python3 /usr/src/app/Auto_attend/attendv2.py > testing.out &" | crontab -

Last command will check script every 5 mins and execute if it was stopped

</details>


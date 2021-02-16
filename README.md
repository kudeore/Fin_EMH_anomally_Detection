# Fin Efficient Market Hypothesis(EMH) anoomaly Detection

An app to exploit opportunities in Financial markets, by finding anomalies in Efficient Market Hypothesis. 
Normally Derivative data in Financial Capital markets follows Efficient Market Hypothesis , where in Option Primiums (Derivatives) follows , black scholes Model. 
But because of intrday volatility or some other reasons , it tends to deviate from EMH . 
Algorithms used in this app , targets such inefficencies and exploits the opportunities . 

## Content
  * [Visuals](#Visuals)
  * [Overview](#Overview)
  * [Cloud Deployment Heroku ](#Cloud_Deployment_Heroku)
  * [Directory Tree](#directory-tree)
  * [Am I missing Something?](#Am-I-missing-Something?)


## Visuals
Link:https://airfarepred.herokuapp.com/

[![](https://i.imgur.com/jk0DgLR.gifv)]
<img target="_blank" src="https://i.imgur.com/Qphlx9g.png" width=400 height=200>
<img target="_blank" src="https://i.imgur.com/EdaG70F.png" width=400 height=200>
<img target="_blank" src="https://i.imgur.com/n0CBQb9.png" width=400 height=200>




## Overview
### Calender Spreads
- Hunts opportunities across various expiry on Call and Put side . 
<img target="_blank" src="https://i.imgur.com/Y5KXMec.png" width=400 height=200>

### Vertical Spreads
- Hunts opportunities across every Expiry on Call and Put side . 
<img target="_blank" src="https://i.imgur.com/3hqerYK.png" width=400 height=200>



## Installation
Install all dependancies using following command after cloning [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Deployement on AWS EC2 Instance 
- Signup on AWS 
- This deployment is done using EC2 instance using Free tier (Ubuntu OS) 

[![](https://i.imgur.com/xAXgRbf.png)](https://aws.amazon.com/)


- Next step is to create app with name as per availability 
- For this particular App ,  we need to creat the environment 
- Create network interface , for public access 
- Push the code to Cloud 
- detail steps are given in the documentation (for documentation visit AWS documentation ) 
- [AWS Documentation](https://docs.aws.amazon.com/)

Importatnt Things to make note of while deploying model to AWS free cloud . 
- Certain SSL requests will be declined by Service provider 
- Eg. For fetching live data from NSE india website , if we try to fetch it from AWS virtual environment, It is giving SSL certificate error 
- Better is to run this App locally for effective use . 


## Directory Tree 
```
├── static 
│   ├── images 
├── templates
│   ├── index.html
│   ├── simple.html
│   ├── simple_put.html
│   ├── simple_VCS.html
│   ├── simple_VPS.html
├── preprocessing.py
├── post_processing.py
├── req.py
├── OC.py
├── app.py
├── README.md
├── page.pkl
├── requirements.txt
```


## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://i.imgur.com/Vgxcuk1.png" width=170>]
[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) [<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) 


## Am I missing Something?

- **Nothing is impossible!**
- please open an [issue](https://github.com/kudeore/Fin_EMH_anomally_Detection/issues) and lets make it better together 
- *Bug reports, feature requests, patches, and well-wishes are always welcome.* :heavy_exclamation_mark:

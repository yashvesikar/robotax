# RoboTax

We have developed a simple tool for extrapolating losses in government tax revenue due to non-taxed automation.
Our Proof-of-Concept has been tailored to address the issue of loss of manufacturing jobs across the United States.
  * Simple User Interface 
  * Intuitive algorithm for calculating "owed tax" by automation

## USAGE
  * We see this being utilized by the United States government in order to review proposed laws and regulations
  * We see this being used by corporations in order to more effectively relocate their manufacturing assets based on the expansive tax code 
  * we see this being used by the financial and legal sector in order to more effectively advise their clients (government and private interests)
## BUILD/INSTALLATION INSTRUCTIONS
### Installation (Mac OS X)

##### Install homebrew
Open terminal and run the following commands in order to install Command Line Tools and homebrew

    xcode-select --install
    
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    
You'll also need some extra libraries installed:

    brew install libtool libxslt libksba openssl

##### Install RVM
Open terminal and run the following command

    \curl -sSL https://get.rvm.io | bash

Close and reopen terminal. Run the following commands        
    
    rvm install 2.2.5

    rvm --default use 2.2.5

And then execute:

    gem install bundle
    
After which we update the gems on the whole system:

    gem update --system


##### Install Python & Flask
Open terminal and run the following command

    brew install python

Once the command finishes, run        
    
    brew install pip

    pip install flask

And then navigate to the project directory:

    python app.py
    
The application should be running at:

    http://localhost:5000/
 

## OTHER SOURCES OF DOCUMENTATION
* Stackoverflow

## Contributor Guide
If you would like to contribute to this nifty project, go [here](https://github.com/yashvesikar/robotax/blob/master/CONTRIBUTING.md)

## License 
MIT Open Source License

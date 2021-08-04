# randomdog

![img](https://raw.githubusercontent.com/ajskateboarder/stuff/main/Screenshot%202021-07-23%20075316.png)

randomdog can edit a `README.md` file daily to display, of course, a random dog image link!
The link is displayed where there is the text: `/dog/`. 
You can use `/dog/` in multiple places but it will show the same image.

### Can it show anything else?

Of course it can! But you will need to do this on your own.

### How do I use this?

The easy way would be to go to the action in [Github Marketplace](https://git.io/JRT3x), get that special yml snippet, and be done. It will run when triggered or every day at 12:00 UTC.

### Self usage

Uhh... requirements:

- Python < 3.6
- Requests
- Git (optional)

To start, download this project or clone it. Then, navigate to the `randomdog` directory and open `config.json`. Fill the values with YOUR information. A repository, it's default branch, and the file you want to show the dog link. Next, take the file content, throw it into `template.raw` and place `/dog/` wherever you like. 

Now you need to create a personal access token to edit the repository file. Once you have that, open up a terminal in `randomdog` and run 

```
python randomdog.py <token>
```

You should see a pushed changed in the repository.

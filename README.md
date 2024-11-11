# HCDE 310 WI23 Final Project

## Pin Your Restaurant Map List
I know every foodie has their exhaustive list of restaurants they want to go to except the list is a
complete mess. In addition, you can easily lose track of which restaurants you have been at and
which ones you still need to try. Restaurant names are not enough to tell you if that is what you
are currently craving or where the restaurant is since you might not feel like driving far.
Currently, you would have to search through every single restaurant and cross-reference them
with google maps or some other app/map and keep going back and forth between your personal
list and your searches. My project aims to provide a collective experience that conveniently
keeps track of restaurants and their locations and information about them all within one place.

## Project Information
This project will be an interactive website that allows users to “save” restaurants around Seattle
on Google Maps. Restaurants can be marked as having gone to it or planning to and will pin the
restaurants on the map to show all their general location. When selecting the pins, information
for the restaurant will be available and then it will be like when you search for a restaurant on
google maps where information such as price, rating, cuisine, distance, etc. will be listed.
The page will be built on google maps api and their preset mapping system (Google Maps
Platform APIs by Platform | Google Developers). In addition, I will collect restaurant
information using yelp’s api (yelp fusion Yelp Fusion | The Most Trusted Local Data Licensing
Platform) and this will aggregate restaurant information.
The Yelp API allows users to search for restaurants and then be able to add them onto Google
Maps for visual representation. Users should be able to search for restaurants, view restaurant
details, pin their favorite restaurants onto a map, and save their selections onto a database.

## Stretch Goals
Filerting: When someone has restaurants pinned all over an area, it can become difficult to
differentiate the pins from each other. Filtering criterias like cuisine, distance from a point, etc.
would allow for more user control over what they see.
Suggestion: Have not looked into Yelp API or aunty similar APIs for restaurant suggestions
based on current interests. Definitely would be difficult to do from scratch and consider what
factors go into suggestions.

## Development Plan
Week 1: Implement Google maps interface, test Yelp API to see if it fits my requirements, setup
interface to allow user to search and read details about a restaurant

Week 2: Create interface for adding restaurant onto google maps, connect Yelp (or alternative)
api to show up when the user expands on a pin, implement a database system like MySQL to
store restaurants

Week 3: Record and prepare for presentation of project, apply test runs
I might actually register restaurants that I want to visit onto my project and use it to see where
restaurants I want to go to are located.


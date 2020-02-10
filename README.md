# Social_network_Thesis_MA
 Informal structure of the firm, network science
 
 This repo shows my ETL and visualisation for my masters dissertation. I have received result data of an informal organsiation questionnaire about a Hungarian logistic firm. It included employees formal position in the firm and their answers for questions like - who do they turn for information / help, or who do they think is trustworthy / examplary etc. The questionnaire was filled out by 3k employees. 
 
 My first challenge was to recategorize the questions as there was a huge correlation between the answers. I have choosen questions that represented flow of information and generated weighted edges out of that, while other questions were transformed into node attributes. 
 
 My original hypothesis was that there is a quadratic connection between number of ties and communication quality, as if one person has more than few connection it means they are good source of information, but if they have too much connection the quality will decrease as there is an optimum for individuals to share information within a certain time. (*The more you talk the less you say*)
 
 Technical challenge was to transform data from a skewed distribution into a normal distribution in order to test my hypothesises with regression in the end. As I had no influence on the questionnaire I had to rely on the received dataset. 
 
 The final report can be found on my linkedin profile. I have received a 5.0/5.0 grade and was supported to put into publication, which might happen soon. 

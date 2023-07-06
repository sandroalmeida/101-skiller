import spacy
from spacy.matcher import Matcher
import json
import re

# Testing variables
text = "Senior software engineerwho we are: siriusxm and its brands (pandora, stitcher, sxm media, adswizz, simplecast, and siriusxm connected vehicle services) are leading a new era of audio entertainment and services by delivering the most compelling subscription and ad-supported audio entertainment experience for listeners -- in the car, at home, and anywhere on the go with connected devices. Our vision is to shape the future of audio, where everyone can be effortlessly connected to the voices, stories and music they love wherever they are. This is the place where a diverse group of emerging talent and legends alike come to share authentic and purposeful songs, stories, sounds and insights through some of the best programming and technology in the world. Our critically-acclaimed, industry-leading audio entertainment encompasses music, sports, comedy, news, talk, live events, and podcasting. No matter their individual role, each of our employees plays a vital part in bringing siriusxms vision to life every day. Siriusxm is the leading audio entertainment company in north america, and the premier programmer and platform for subscription and digital advertising-supported audio products. Siriusxms platforms collectively reach approximately 150 million listeners, the largest digital audio audience across paid and free tiers in north america, and deliver music, sports, talk, news, comedy, entertainment and podcasts. Pandora, a subsidiary of siriusxm, is the largest ad-supported audio entertainment streaming service in the u. S. Siriusxm's subsidiaries stitcher, simplecast and adswizz make it a leader in podcast hosting, production, distribution, analytics and monetization. The companys advertising sales organization, which operates as sxm media, leverages its scale, cross-platform sales organization and ad tech capabilities to deliver results for audio creators and advertisers. Siriusxm, through sirius xm canada holdings, inc. , also offers satellite radio and audio entertainment in canada. In addition to its audio entertainment businesses, siriusxm offers connected vehicle services to automakers. How youll make an impact: we are looking for a senior software engineer to join the siriusxm and automotive continuity team within the platform services organization. The sxm & auto continuity team is responsible for building high throughput, highly available microservices on siriusxms api platform that are critical to the user experience. These microservices and apis power multiple clients for siriusxm and pandora, including automotive clients, streaming apps, and connected streaming devices, that collectively reach millions of users. What youll do: work with a highly collaborative group of engineers in squad organization. Innovate to build performant solutions that continue to scale to the increasing demandsof the business. Contribute to a healthy engineering culture and drive best practices. Lead high-level architecture discussions and planning sessions. Strive to develop simple solutions to complex problems. Ensure team-wide code quality through code reviews and pr feedback. Exhibit accountability at both a personal and team level. Author and provide feedback on technical proposals and root cause analyses. Participate in maintenance and on-call rotation on a limited basis. What youll need: bs in engineering, computer science, information systems, or other technically related field. Equivalent experience and/or degrees in other technical fields will be evaluated and considered. Minimum of five years professional experience. Expertise in one or more modern programming languages, preferably scala and java. Familiarity with functional programming paradigms. Familiarity with frameworks such as spring bootexperience designing and implementing restful web apis in an enterprise setting. Deep understanding of the software development lifecycle, including the use of sourcecontrol, ci/cd and various testing approaches. Deep distributed systems knowledge, having supported multiple high-throughputsystems in a production setting. Experience in building highly scalable and highly performant microservices. Experience with aws in a production setting, preferably having leveraged offerings forcompute, databases, storage, containers and serverless technologies. Experience with asynchronous programming models, preferably those that supporthigh-throughput systems running in a docker environment. Pragmatic approach to weighing engineering tradeoffs versus business needs. Persistent sense of curiosity to understand why something is and needs to be. Accountability and a sense of extreme ownership that doesnt end after the system isdeployed to production. Excellent written and verbal communication skills. Must have legal right to work in the u. S. At siriusxm, we carefully consider a wide range of factors when determining compensation, including your background and experience. These considerations can cause your compensation to vary. We expect the base salary for this position to be in the range of $142,500 to $220,000 and will depend on your skills, qualifications, and experience. Additionally, this role might be eligible for discretionary short-term and long-term incentives. We encourage all interested candidates to apply. Our goal at siriusxm is to provide and maintain a work environment that fosters mutual respect, professionalism and cooperation. Siriusxm is an equal opportunity employer that does not discriminate on the basis of actual or perceived race, creed, color, religion, national origin, ancestry, alienage or citizenship status, age, disability or handicap, sex, gender identity, maritalstatus, familial status, veteran status, sexual orientation or any other characteristic protected by applicable federal, state or local laws. Our goal at siriusxm is to provide and maintain a work environmentthatfosters mutualrespect, professionalism andcooperation. Siriusxmisan equal opportunity employerthat doesnotdiscriminate onthe basis of actualorperceived race, creed, color, religion, national origin, ancestry, alienage orcitizenship status, age, disability or handicap, sex, genderidentity, marital status, familial status, veteranstatus, sexual orientation or any other characteristicprotected by applicable federal, state or local laws. The requirements and duties described abovemaybemodified or waived by the company in its solediscretion without notice."
regex_string = "computer\s+science"
json_pattern = '[{"LOWER": "computer"}, {"LOWER": "science"}]'

# Load a language model
nlp = spacy.load("en_core_web_lg")

# Create a doc object for skill matching process
doc = nlp(text)

# Printing tokens
# for token in doc:
#     print(token.is_punct, token.text, token.pos_, token.dep_)

# Create a matcher object
matcher = Matcher(nlp.vocab, validate=True)
matcher.add("test", [json.loads(json_pattern)])

# Find all the skills matches of the pattern in the doc
matches = matcher(doc)

# Collect the unique skill names and unmatched strings in a set
official_skill_list = set()
not_official_skill_list = set()
for match_id, start, end in matches:
    match_text = doc[start:end].text
    print(match_text)
    if(re.match(regex_string, match_text.lower(), re.IGNORECASE)):
        official_skill_list.add(match_text)
    else:
        not_official_skill_list.add(match_text)

# Printing results
if(official_skill_list):
    print("official_skill_list")
    print(official_skill_list)
if(not_official_skill_list):
    print("not_official_skill_list")
    print(not_official_skill_list)
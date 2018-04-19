from flask import Flask, jsonify, request

app = Flask(__name__)

consultants = [
  { 
    'name': 'Kristoffer Risa',
    'aboutMe':'Consultant in Visma Retail. SQL and Csharp guru',
    'myProjects':['bla', 'bla', 'bla'],
    'mySkills':['java','csharp','php'],
    'askMeAbout':['C#', 'Java', 'Sql', 'html', 'REST api'] 
  },
  { 'name': 'Nils Nilsen',
    'aboutMe':'Consultant in Visma Retail.',
    'myProjects':['bla', 'bla', 'bla'],
    'mySkills':['ruby','css','php'],
    'askMeAbout':['ruby', 'css', 'php']
   }
]

@app.route('/consultants')
def get_consultants():
  myList = []
  args = request.args
  skill = args['skill']
  print (args) # For debugging
  if skill != 'showAll':
    for each in consultants:
      try:
          if skill in each['mySkills']: 
             myList.append(each)
      except KeyError:
          pass
    return jsonify(myList)
  else:
    return jsonify(consultants)


@app.route('/consultants', methods=['POST'])
def add_consultant():
  consultants.append(request.get_json())
  return '', 204


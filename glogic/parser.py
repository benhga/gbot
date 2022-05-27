import json


# parsers for seeding the database, called from manager
def questions_parse(json_string, db_table):
    questions = []
    questions_dicts = json.loads(json_string).get('questions')
    for question_dict in questions_dicts:
        body = question_dict['body']
        questions.append(db_table(content=body))
    return questions


# data
TRAINING_DATA_FILE = "sample data.csv"
PIPELINE_NAME = 'decision_trees'

TARGET = [ 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10', 'Y11', 'Y12', 'Y13', 'Y14', 'Y15', 'Y16', 'Y17', 'Y18', 'Y19',
'Y20', 'Y21', 'Y22', 'Y23', 'Y24', 'Y25', 'Y26', 'Y27', 'Y28', 'Y29','Y30', 'Y31', 'Y32', 'Y33']

CLASS_LIST = ['ADHD','Dementia','Substance Abuse','Schizophrenia and other psychotic disorders',
				'Bipolar Disorder','Depression','Panic Disorder','Specific Phobia/Agoraphobia',
				'Acute Stress Disorder','PTSD','GAD','Facititious disorder', 'Dissociative Fugue/Depersonalization',
				'Dissociative Identity Disorder','Eating Disorder','Nightmare Disorder','Narcolepsy','Breathing Related Sleep Disorder (BRSD)',
				'Sleepwalking','Pyromania','Trichotillomania','Pathological Gambling','Kleptomania','Intermittent Explosive Disorder',
				'Borderline Personality Disorder','Narcissistic Personality Disorder','Dependent Personality Disorder','Avoidant Personality Disorder',
				'Paranoid Personality Disorder','Histrionic Personality Disorder','Histrionic Personality Disorder','Antisocial Behavior','Schizoid Personality Disorder'
]

#print(len(CLASS_LIST))
# input variables 
FEATURES = [
	'ATTN', 
	'IMPULSV-1', 
	'MEMORY',
    'DEMEN-1',
    'SCHIZO-1',
    'DEMEN-2',
    'SUBSTANS-1',
    'SUBSTANS-2',
    'SUBSTANS-3', 
    'SCHIZO-2', 
    'BIPOLAR-1', 
    'BIPOLAR-2', 
    'DEPR-1', 
    'PA',
    'FEAR', 
    'ANX', 
    'PTSD', 
    'DETACH', 
    'PTSD-2', 
    'BLANK', 
    'APPEAR FEAR', 
    'FACITIOUS', 
    'MULTI PERSON',
    'SLEEP DISORDR', 
    'NARCOLEP', 
    'SLEEP PARAL-1', 
    'SLEEP PARAL-2', 
    'SNORE',
    'SLEEP WALK', 
    'PYRO', 
    'HAIR LSS', 
    'GAMBLE', 
    'STEAL', 
    'IMPULSV-2',
    'SUICIDE', 
    'ALONE', 
    'NARCISSISTIC', 
    'COLD', 
    'DEPENDENT', 
    'DEPENDENT-2',
    'PARANOID', 
    'ECCENTRIC', 
    'OCD', 
    'ANTISOCIAL-1', 
    'ANTISOCIAL-2', 
    'LYING',
    'SCHIZOAFFECT', 
    'DEMEN-3', 
    'PTSD-1', 
    'Patient'
]

DROP_FEATURES = [
	'Patient',
	'MEMORY',
	'DEMEN-2',
	'SLEEP PARAL-1',
	'SUICIDE',
	'LYING',
	'PTSD-1'
]

NUMERICAL_VARS_WITH_NA = [
    'ATTN', 
	'IMPULSV-1', 
	'MEMORY',
    'DEMEN-1',
    'SCHIZO-1',
    'DEMEN-2',
    'SUBSTANS-1',
    'SUBSTANS-2',
    'SUBSTANS-3', 
    'SCHIZO-2', 
    'BIPOLAR-1', 
    'BIPOLAR-2', 
    'DEPR-1', 
    'PA',
    'FEAR', 
    'ANX', 
    'PTSD', 
    'DETACH', 
    'BLANK',  
    'APPEAR FEAR', 
    'FACITIOUS', 
    'MULTI PERSON',
    'SLEEP DISORDR', 
    'NARCOLEP', 
    'SLEEP PARAL-1', 
    'SLEEP PARAL-2', 
    'SNORE',
    'SLEEP WALK', 
    'PYRO', 
    'HAIR LSS', 
    'GAMBLE', 
    'STEAL', 
    'IMPULSV-2',
    'SUICIDE', 
    'ALONE', 
    'NARCISSISTIC', 
    'COLD', 
    'DEPENDENT', 
    'DEPENDENT-2',
    'PARANOID', 
    'ECCENTRIC', 
    'OCD', 
    'ANTISOCIAL-1', 
    'ANTISOCIAL-2', 
    'LYING',
    'SCHIZOAFFECT', 
    'DEMEN-3', 
    'PTSD-1',  
]

CATEGORICAL_VARS_WITH_NA = [ 
    'PTSD-2'
]

CATEGORICAL_VARS = [  
    'PTSD-2' 
]

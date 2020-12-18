import configparser
import json
def update_json():
    config = configparser.ConfigParser()
    config.read('config.ini')
    rabbit_default_dict = {}
    fox_default_dict = {}

    rabbit_default_dict['life_expectancy_months'] = config['default_rabbits'].getint('life_expectancy_months')
    rabbit_default_dict['maturity_age_months'] = config['default_rabbits'].getint('maturity_age_months')
    rabbit_default_dict['sim_duration_years'] = config['default_rabbits'].getint('sim_duration_years')
    rabbit_default_dict['num_starting_rabbits'] = config['default_rabbits'].getint('num_starting_rabbits')
    rabbit_default_dict['sim_rate'] = config['default_rabbits'].getint('sim_rate')
    rabbit_default_dict['max_num_babies'] = config['default_rabbits'].getint('max_num_babies')
    rabbit_default_dict['ratio_male_to_female'] = config['default_rabbits'].getfloat('ratio_male_to_female')
    rabbit_default_dict['male_availability_recharge'] = config['default_rabbits'].getint('male_availability_recharge')
    rabbit_default_dict['female_availability_recharge'] = config['default_rabbits'].getint('female_availability_recharge')
    rabbit_default_dict['female_fertility'] = config['default_rabbits'].getfloat('female_fertility')

    fox_default_dict['life_expectancy_months'] = config['default_foxes'].getint('life_expectancy_months')
    fox_default_dict['maturity_age_months'] = config['default_foxes'].getint('maturity_age_months')
    fox_default_dict['integrating_month'] = config['default_foxes'].getint('integrating_month')
    fox_default_dict['rabbit_eating_maturity'] = config['default_foxes'].getint('rabbit_eating_maturity')
    fox_default_dict['num_starting_foxes'] = config['default_foxes'].getint('num_starting_foxes')
    fox_default_dict['female_fertility'] = config['default_foxes'].getfloat('female_fertility')
    fox_default_dict['max_num_babies'] = config['default_foxes'].getint('max_num_babies')
    fox_default_dict['ratio_male_to_female'] = config['default_foxes'].getfloat('ratio_male_to_female')
    fox_default_dict['male_availability_recharge'] = config['default_foxes'].getint('male_availability_recharge')
    fox_default_dict['female_availability_recharge'] = config['default_foxes'].getint('female_availability_recharge')
    fox_default_dict['num_rabbits_eaten'] = config['default_foxes'].getint('num_rabbits_eaten')





    with open('rabbit_project/rabbit_default.json', 'w+') as jsonfile:
        json.dump(rabbit_default_dict, jsonfile)



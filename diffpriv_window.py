from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', 960)
Config.set('graphics', 'height', 540)
Config.set('kivy', 'window_icon', 'kivy_epsilon.png')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from matplotlib import pyplot as plt
from random import randint, uniform, shuffle
import random
import numpy as np


def coin_flip(input_list):
    randomized_list = input_list[:]
    for member in range(len(randomized_list)):
        first_rand = randint(0, 1)
        if first_rand == 1:
            pass
        else:
            second_rand = randint(0, 1)
            if second_rand == 1:
                randomized_list[member] = 1
            else:
                randomized_list[member] = 0
                pass
    real_yes_percent = round(randomized_list.count(1) * 100/len(randomized_list), 1)
    with_approximation = round(real_yes_percent * 2 - 50, 1)
    return [real_yes_percent, with_approximation]


def isfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


class MainWindow(Screen):
    pass


class FirstWindow(Screen, Widget):
    main_members_list = []
    dump = 0
    amount_survey_members = 0
    chart1 = []
    chart2 = []

    def survey_members_generation(self):
        if self.ids.enter_number.text != '':
            random_yes_percent = 0
            if self.ids.enter_number.text.isnumeric():
                if 100 <= int(self.ids.enter_number.text) <= 5000:
                    self.dump = 0
                    self.ids.result_1.text = "N/A"
                    self.ids.result_2.text = "N/A"
                    self.ids.result_3.text = "N/A"
                    self.ids.result_4.text = "N/A"
                    self.ids.result_5.text = "N/A"
                    self.ids.result_6.text = "N/A"
                    self.ids.result_7.text = "N/A"
                    self.ids.result_8.text = "N/A"
                    self.ids.result_9.text = "N/A"
                    self.ids.result_10.text = "N/A"
                    self.real_yes_result.text = "N/A"
                    self.chart1 = []
                    self.chart2 = []
                    self.amount_survey_members = int(self.ids.enter_number.text)
                    self.ids.enter_number.hint_text = self.ids.enter_number.text
                    self.ids.enter_number.text = ''
                    if random_yes_percent == 0:
                        random_yes_percent = round(uniform(1, 100), 1)
                    amount = random_yes_percent * self.amount_survey_members / 100
                    self.main_members_list = [1] * round(amount) + [0] * (self.amount_survey_members - round(amount))
                    shuffle(self.main_members_list)
                else:
                    self.ids.enter_number.hint_text = 'Մուտքագրել'
                    self.ids.enter_number.text = ''
                    self.amount_survey_members = 0
            else:
                self.ids.enter_number.text = ''

    def results_10(self, start):
        if len(self.main_members_list) != 0:
            if self.dump < 11:
                self.dump += start
            if self.dump == 1:
                rand_list = coin_flip(self.main_members_list)
                self.chart1.append(rand_list[0])
                self.chart2.append(rand_list[1])
                self.ids.result_1.text = f"{rand_list[0]}% | {rand_list[1]}%"
            elif self.dump == 2:
                rand_list = coin_flip(self.main_members_list)
                self.chart1.append(rand_list[0])
                self.chart2.append(rand_list[1])
                self.ids.result_2.text = f"{rand_list[0]}% | {rand_list[1]}%"
            elif self.dump == 3:
                rand_list = coin_flip(self.main_members_list)
                self.chart1.append(rand_list[0])
                self.chart2.append(rand_list[1])
                self.ids.result_3.text = f"{rand_list[0]}% | {rand_list[1]}%"
            elif self.dump == 4:
                rand_list = coin_flip(self.main_members_list)
                self.chart1.append(rand_list[0])
                self.chart2.append(rand_list[1])
                self.ids.result_4.text = f"{rand_list[0]}% | {rand_list[1]}%"
            elif self.dump == 5:
                rand_list = coin_flip(self.main_members_list)
                self.chart1.append(rand_list[0])
                self.chart2.append(rand_list[1])
                self.ids.result_5.text = f"{rand_list[0]}% | {rand_list[1]}%"
            elif self.dump == 6:
                rand_list = coin_flip(self.main_members_list)
                self.chart1.append(rand_list[0])
                self.chart2.append(rand_list[1])
                self.ids.result_6.text = f"{rand_list[0]}% | {rand_list[1]}%"
            elif self.dump == 7:
                rand_list = coin_flip(self.main_members_list)
                self.chart1.append(rand_list[0])
                self.chart2.append(rand_list[1])
                self.ids.result_7.text = f"{rand_list[0]}% | {rand_list[1]}%"
            elif self.dump == 8:
                rand_list = coin_flip(self.main_members_list)
                self.chart1.append(rand_list[0])
                self.chart2.append(rand_list[1])
                self.ids.result_8.text = f"{rand_list[0]}% | {rand_list[1]}%"
            elif self.dump == 9:
                rand_list = coin_flip(self.main_members_list)
                self.chart1.append(rand_list[0])
                self.chart2.append(rand_list[1])
                self.ids.result_9.text = f"{rand_list[0]}% | {rand_list[1]}%"
            elif self.dump == 10:
                rand_list = coin_flip(self.main_members_list)
                self.chart1.append(rand_list[0])
                self.chart2.append(rand_list[1])
                self.ids.result_10.text = f"{rand_list[0]}% | {rand_list[1]}%"

    def real_yes_percent(self):
        if self.amount_survey_members != 0:
            self.ids.real_yes_result.text = str(round(self.main_members_list.count(1) * 100 /
                                                      self.amount_survey_members, 1)) + '%'

    def bar_chart(self, which_one):
        if self.amount_survey_members != 0 and len(self.chart1) == 10 and len(self.chart2) == 10:
            plt.style.use('default')
            plt.figure(figsize=(10, 8), facecolor='#d8cbbb')
            ax = plt.axes()
            ax.set_facecolor('#d8cbbb')
            ax.spines['bottom'].set_color('#1c4864')
            ax.spines['top'].set_color('#1c4864')
            ax.spines['right'].set_color('#1c4864')
            ax.spines['left'].set_color('#1c4864')
            ax.xaxis.label.set_color('#1c4864')
            ax.yaxis.label.set_color('#1c4864')
            ax.tick_params(axis='x', colors='#1c4864')
            ax.tick_params(axis='y', colors='#1c4864')
            x = [el for el in range(1, 11)]
            y = round(self.main_members_list.count(1) * 100 / self.amount_survey_members, 1)
            if which_one == 1:
                plot = plt.bar(x, self.chart1, color='#2d8183',
                               label='Պատահականեցված հարցման «Այո» պատասխանի արդյունքները')
                for value, header in zip(plot, self.chart1):
                    height = value.get_height()
                    plt.text(value.get_x() + value.get_width() / 2,
                             height, str(header) + '%', ha='center', va='bottom', size=12, color='#1c4864')
                plt.axhline(y=y, linewidth=1, color='#910c07', label='Հարցման «Այո» պատասխանի իրական արդյունքը')
                plt.text(5.5, y + .5, f'{y}%', size=12, color='#910c07', ha='center', va='center')
                plt.xticks(x)
            elif which_one == 2:
                plot = plt.bar(x, self.chart2, color='#2d8183',
                               label='Պատահականեցված հարցման «Այո» պատասխանի մոտավոր արդյունքները')
                for value, header in zip(plot, self.chart2):
                    height = value.get_height()
                    plt.text(value.get_x() + value.get_width() / 2,
                             height, str(header) + '%', ha='center', va='bottom', size=12, color='#1c4864')
                plt.axhline(y=y, linewidth=1, color='#910c07', label='Հարցման «Այո» պատասխանի իրական արդյունքը')
                plt.text(5.5, y + .5, f'{y}%', size=12, color='#910c07', ha='center', va='center')
                plt.xticks(x)
            plt.xlabel('\u2116 Փորձ', fontweight='bold', size=12)
            plt.ylabel('Արդյունք', fontweight='bold', size=12)
            plt.title('Մետաղադրամի նետմամբ պատահականեցված պատասխանի x10 փորձերը',
                      size=12, color='#1c4864', fontweight='bold')
            ld = plt.legend(facecolor='#e4dacf', loc='lower left')
            plt.setp(ld.get_texts(), color='#1c4864', fontweight='bold')
            plt.tight_layout()
            plt.show()


class SecondWindow(Screen, Widget):
    dump_mean = 0
    dump_sum = 0
    amount_survey_members = 0
    database = list()
    parallel_databases = list()
    mean_query_result = 0
    mean_cache_result = 0
    sum_query_result = 0
    sum_cache_result = 0
    mean_sensitivity = 0
    sum_sensitivity = 0
    mean_epsilon_input = 0
    sum_epsilon_input = 0

    def survey_members_generation(self):
        if self.ids.enter_number.text != '':
            if self.ids.enter_number.text.isnumeric():
                if 10 <= int(self.ids.enter_number.text) <= 5000:
                    self.ids.mean_query_output.text = "N/A"
                    self.ids.mean_query_output.color = [28/255.0, 72/255.0, 100/255.0, 1]
                    self.ids.sum_query_output.text = "N/A"
                    self.ids.sum_query_output.color = [28/255.0, 72/255.0, 100/255.0, 1]
                    self.ids.mean_sens_output.text = "N/A"
                    self.ids.sum_sens_output.text = "N/A"
                    self.ids.mean_epsilon_input_button.hint_text = "0-ից մեծ"
                    self.ids.sum_epsilon_input_button.hint_text = "0-ից մեծ"
                    self.ids.mean_laplace_noise_output.text = "N/A"
                    self.ids.sum_laplace_noise_output.text = "N/A"
                    self.dump_mean = 0
                    self.dump_sum = 0
                    self.database = list()
                    self.parallel_databases = list()
                    self.mean_query_result = 0
                    self.sum_query_result = 0
                    self.mean_sensitivity = 0
                    self.sum_sensitivity = 0
                    self.mean_epsilon_input = 0
                    self.sum_epsilon_input = 0
                    self.amount_survey_members = int(self.ids.enter_number.text)
                    self.ids.enter_number.hint_text = self.ids.enter_number.text
                    self.ids.enter_number.text = ''
                    db_start = random.randint(100, 250)
                    db_end = random.randint(750, 1000)
                    self.database = [round(random.uniform(db_start, db_end), 2)
                                     for _ in range(self.amount_survey_members)]
                    for i in range(len(self.database)):
                        pdb = self.database[0:i] + self.database[i + 1:]
                        self.parallel_databases.append(pdb)
                else:
                    self.ids.enter_number.hint_text = 'Մուտքագրել'
                    self.ids.enter_number.text = ''
                    self.amount_survey_members = 0
            else:
                self.ids.enter_number.text = ''

    def mean_query(self):
        if len(self.database) != 0 and self.dump_mean == 0:
            self.mean_query_result = round(sum(self.database) / len(self.database), 2)
            self.mean_cache_result = round(sum(self.database) / len(self.database), 2)
            self.ids.mean_query_output.text = str(self.mean_query_result)
            self.dump_mean += 1
        if self.dump_mean > 0:
            self.ids.mean_query_output.text = str(self.mean_cache_result)
            self.ids.mean_query_output.color = [28 / 255.0, 72 / 255.0, 100 / 255.0, 1]

    def sum_query(self):
        if len(self.database) != 0 and self.dump_sum == 0:
            self.sum_query_result = round(sum(self.database), 2)
            self.sum_cache_result = round(sum(self.database), 2)
            self.ids.sum_query_output.text = str(self.sum_query_result)
            self.dump_sum += 1
        if self.dump_sum > 0:
            self.ids.sum_query_output.text = str(self.sum_cache_result)
            self.ids.sum_query_output.color = [28 / 255.0, 72 / 255.0, 100 / 255.0, 1]

    def mean_sens(self):
        if self.mean_query_result != 0:
            for pdb in self.parallel_databases:
                pdb_result = sum(pdb) / len(pdb)
                db_distance = round(abs(pdb_result - self.mean_query_result), 2)
                if db_distance > self.mean_sensitivity:
                    self.mean_sensitivity = db_distance
            self.ids.mean_sens_output.text = str(self.mean_sensitivity)

    def sum_sens(self):
        if self.sum_query_result != 0:
            for pdb in self.parallel_databases:
                pdb_result = sum(pdb)
                db_distance = round(abs(pdb_result - self.sum_query_result), 2)
                if db_distance > self.sum_sensitivity:
                    self.sum_sensitivity = db_distance
            self.ids.sum_sens_output.text = str(self.sum_sensitivity)

    def mean_epsilon(self):
        if self.ids.mean_epsilon_input_button.text != '':
            if isfloat(self.ids.mean_epsilon_input_button.text) and '-' not in self.ids.mean_epsilon_input_button.text:
                if self.ids.mean_epsilon_input_button.text != '0':
                    self.mean_epsilon_input = float(self.ids.mean_epsilon_input_button.text)
                    self.ids.mean_epsilon_input_button.hint_text = self.ids.mean_epsilon_input_button.text
                    self.ids.mean_epsilon_input_button.text = ''
                else:
                    self.ids.mean_epsilon_input_button.hint_text = '0-ից մեծ'
                    self.ids.mean_epsilon_input_button.text = ''
                    self.mean_epsilon_input = 0
            else:
                self.ids.mean_epsilon_input_button.text = ''

    def sum_epsilon(self):
        if self.ids.sum_epsilon_input_button.text != '':
            if isfloat(self.ids.sum_epsilon_input_button.text) and '-' not in self.ids.sum_epsilon_input_button.text:
                if self.ids.sum_epsilon_input_button.text != '0':
                    self.sum_epsilon_input = float(self.ids.sum_epsilon_input_button.text)
                    self.ids.sum_epsilon_input_button.hint_text = self.ids.sum_epsilon_input_button.text
                    self.ids.sum_epsilon_input_button.text = ''
                else:
                    self.ids.sum_epsilon_input_button.hint_text = '0-ից մեծ'
                    self.ids.sum_epsilon_input_button.text = ''
                    self.sum_epsilon_input = 0
            else:
                self.ids.sum_epsilon_input_button.text = ''

    def mean_laplace_noise(self):
        if self.mean_epsilon_input != 0 and self.mean_sensitivity != 0:
            beta = round(self.mean_sensitivity / self.mean_epsilon_input, 2)
            noise = round(np.random.laplace(0, beta, 1)[0], 2)
            self.ids.mean_laplace_noise_output.text = str(noise)
            self.ids.mean_query_output.text = str(round(noise + self.mean_query_result, 2))
            self.ids.mean_query_output.color = [145/255.0, 12/255.0, 7/255.0, 1]

    def sum_laplace_noise(self):
        if self.sum_epsilon_input != 0 and self.sum_sensitivity != 0:
            beta = round(self.sum_sensitivity / self.sum_epsilon_input, 2)
            noise = round(np.random.laplace(0, beta, 1)[0], 2)
            self.ids.sum_laplace_noise_output.text = str(noise)
            self.ids.sum_query_output.text = str(round(noise + self.sum_query_result, 2))
            self.ids.sum_query_output.color = [145 / 255.0, 12 / 255.0, 7 / 255.0, 1]


class WindowManager(ScreenManager):
    pass


class DifferentialPrivacy(App):
    Window.clearcolor = (216 / 255.0, 203 / 255.0, 187 / 255.0, 1)

    def build(self):
        return Builder.load_file('diffpriv_window.kv')


if __name__ == '__main__':
    DifferentialPrivacy().run()

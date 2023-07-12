import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
areas = ['ML Ops', 'Data Pipelines', 'Databases', 
         'Data Tools', 'Storytelling', 'Data Visualization',
         'Business Insights (BI)', 
         'Metrics & Reporting', 'Experimentation', 'Inference', 
         'Stats & ML Modeling', 'Model Deployment']
Data_Engineer = [40,100,100,
                 100,10,10,
                 20,30,10,
                 10,10,30]
Data_Scientist = [40,30,20,
                  5,30,40,
                  50,60,80,
                  90,100,50]
Data_Analyst = [5,5,5,
                5,100,100,
                100,100,50,
                30,20,5]
ML_Engineer = [100,50,30,
               25,20,20,
               20,30,40,
               50,70,100]
me = [20,30,40,
      10,70,80,
      80,100,60,
      90,100,50]
angles=np.linspace(0,2*np.pi,len(areas), endpoint=False)
angles=np.concatenate((angles,[angles[0]]))
print(angles)
print(len(angles))
me.append(me[0])
Data_Engineer.append(Data_Engineer[0])
Data_Scientist.append(Data_Scientist[0])
ML_Engineer.append(ML_Engineer[0])
Data_Analyst.append(Data_Analyst[0])
areas.append(areas[0])
fig, (ax, ax2) = plt.subplots(1, 2,  subplot_kw={'projection': 'polar'}, figsize=(15, 10))
#DE Plot
engineer_plot, = ax.plot(angles, Data_Engineer, 'o-', color='g', linewidth=1, label='Data Engineer')
#DS Plot
scientist_plot, = ax.plot(angles, Data_Scientist, 'o-', color='orange', linewidth=1, label='Data Scientist')
#DA Plot
analyst_plot, = ax.plot(angles, Data_Analyst, 'o-', color='b', linewidth=1, label='Data Analyst')
#ML Plot
ml_plot, = ax.plot(angles, ML_Engineer, 'o-', color='r', linewidth=1, label='ML Engineer')
ax.set_thetagrids(angles * 180/np.pi, areas)
ax.set_title('Professional Areas')
ax.set_xticks(angles)
ax.set_xticklabels(areas)
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
#ME Plot
me_plot, = ax2.plot(angles, me, 'o-', color='purple', linewidth=1, label='Me')
ax2.set_thetagrids(angles * 180/np.pi, areas)
ax2.set_xticks(angles)
ax2.set_xticklabels(areas)
ax2.set_title('My Skills')
ax2.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
# Customize polar plot
ax.spines['polar'].set_color('black')
ax.spines['polar'].set_linewidth(0.5)
ax2.spines['polar'].set_color('black')
ax2.spines['polar'].set_linewidth(0.5)
plt.grid(True)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax2.set_facecolor('white')
plt.tight_layout()
plt.show()
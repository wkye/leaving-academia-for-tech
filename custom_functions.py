from serpapi import GoogleSearch
import pandas as pd
import plotly.graph_objects as go

def query_google_jobs(q, location, api_key, engine, chips, n_search):
    combined_queries = []
    for i in range(0,n_search,10):
        jobs_results = GoogleSearch({"q":q,
                                     "location":location,
                                     "api_key":api_key,
                                     "engine":engine,
                                     "chips":chips,
                                     "start":i}
                                     ).get_dict()
        combined_queries = combined_queries + jobs_results['jobs_results']
    return combined_queries


def clean_google_jobs_query(df):
    job_dict_final = {'title':[], 'description':[], 'company_name':[]}
    for i in df:
        job_dict = {key: i[key] if key in i.keys() else '' for key in ['title','description','company_name']}
        job_dict_final['title'].append(job_dict['title'])
        job_dict_final['description'].append(job_dict['description'])
        job_dict_final['company_name'].append(job_dict['company_name'])
    jobs_df = pd.DataFrame(job_dict_final)
    # basic regex cleaning to remove capitalization
    jobs_df['description'] = jobs_df['description'].str.lower()
    return jobs_df


def create_job_search_word_figure(df, search_terms, display_figure):
    percentage_list = []
    for term in search_terms:
        percentage = df['description'].str.contains(term).mean()*100
        percentage_list.append(percentage)
    search_percentages_df = pd.DataFrame({'term':search_terms, 'percentage':percentage_list}).sort_values('percentage', ascending=False)
    data = [go.Bar(x=search_percentages_df['term'], y=search_percentages_df['percentage'])]
    fig1 = go.Figure(data = data)
    fig1.update_layout(
        xaxis = {'title':'Search Term'},
        yaxis = {'title':'Percentage of Search Term Shows Up'}
    )
    fig1.write_image("static/leaving-academia/fig1.png")
    if display_figure: return fig1

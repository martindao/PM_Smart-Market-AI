import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def show_heatmap(comp_comp=True):
    """Shows the heatmap for the similarity"""
    if comp_comp:
        df = pd.read_csv('competitor_competitor_similarity.csv')
        # Comment this line if the scores are already between 0 and 100
        df['similarity_score'] = 100 * df['similarity_score']
        c1 = ['competitor_1']
        c2 = ['competitor_2']
        swap = df.rename(columns={**dict(zip(c1, c2)), **dict(zip(c2, c1))})
        df = pd.concat([swap, df]).sort_index(ignore_index=True)
        df_pivot = df.pivot(index='competitor_1', columns='competitor_2', values='similarity_score')
    else:
        df = pd.read_csv('competitor_influencer_similarity.csv')
        # Comment this line if the scores are already between 0 and 100
        df['similarity_score'] = 100 * df['similarity_score']
        # df = df[df['competitor_name'] != 'indisupplements']
        df_pivot = df.pivot(index='competitor_name', columns='influencer_name', values='similarity_score')

    # df_pivot['null_count'] = df_pivot.isnull().sum()
    # df_pivot = df_pivot.sort_values('null_count', ascending=False).drop('null_count', axis=1)

    # print(df_pivot)
    ax = sns.heatmap(df_pivot, annot=True, cmap='Blues_r', cbar=False)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

    if comp_comp:
        plt.title('Competitor-Competitor Similarity')
        plt.xlabel('Competitor')
        plt.ylabel('Competitor')
    else:
        plt.title('Competitor-Influencer Similarity')
        plt.ylabel('Competitor')
        plt.xlabel('Influencer')
    plt.tight_layout()
    plt.show()


# show_heatmap(comp_comp=False)

# [2020-11-05] (Influencer) schedule note: Enhance similarity analysis for Influencer

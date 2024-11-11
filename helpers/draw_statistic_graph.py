import matplotlib.pyplot as plt
import seaborn as sns

def Compare_Features_Occurrences(before_data, current_data=None):
    # Calculate feature occurrences for X_train_data and X_test_data
    before_removing_feature_count = before_data.count()


    if current_data is not None:
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 6), sharey=True)
        # Plot occurrences for before_removing_data
        before_removing_feature_count.plot(kind='bar', color='skyblue', ax=axes[0])
        axes[0].set_title(f'Occurrences of Each Feature Before removing_outliers (Data Length: {len(before_data)})')
        axes[0].set_xlabel('Features')
        axes[0].set_ylabel('Occurrences')
        axes[0].tick_params(axis='x', rotation=90)

        # Plot occurrences for current_data
        after_removing_train_feature_count = current_data.count()
        after_removing_train_feature_count.plot(kind='bar', color='lightcoral', ax=axes[1])
        axes[1].set_title(f'Occurrences of Each Feature After removing_outliers (Data Length: {len(current_data)})')
        axes[1].set_xlabel('Features')
        axes[1].tick_params(axis='x', rotation=90)
    else:
        # Create a figure with only one subplot if `cur_data` is not provided
        fig, ax = plt.subplots(figsize=(8, 6))
        before_removing_feature_count.plot(kind='bar', color='skyblue', ax=ax)
        ax.set_title(f'Occurrences of Each Feature (Data Length: {len(before_data)})')
        ax.set_xlabel('Features')
        ax.set_ylabel('Occurrences')
        ax.tick_params(axis='x', rotation=90)

    # Adjust layout
    plt.tight_layout()
    plt.show()

def Outlier_Values_Visulization(before_data, current_data=None):

    if current_data is not None:
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))
        sns.boxplot(data=before_data, ax=axes[0])
        axes[0].set_title("Before Removing Outlier Values")
        axes[0].tick_params(axis='x', rotation=90)

        sns.boxplot(data=current_data, ax=axes[1])
        axes[1].set_title("After Removing Outlier Values")
        axes[1].tick_params(axis='x', rotation=90)
        print(len(current_data))
    else:
        fig, ax = plt.subplots(figsize=(10, 6))
        
        sns.boxplot(data=before_data, ax=ax)
        ax.set_title("Before Removing Outlier Values")
        ax.tick_params(axis='x', rotation=90)


    plt.tight_layout()
    plt.show()

def Outlier_Features_Occurrences(current_data):

    print (current_data)
    fig, ax = plt.subplots(figsize=(8, 6))
    current_data.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title(f'Occurrences of Each Outlier Feature (Total Occurrence: {current_data.sum()})')
    ax.set_xlabel('Features')
    ax.set_ylabel('Occurrences')
    ax.tick_params(axis='x', rotation=90)

    # Adjust layout
    plt.tight_layout()
    plt.show()

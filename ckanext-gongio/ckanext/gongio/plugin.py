import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


def most_popular_organizations():
    '''Return a sorted list of the organizations with the most datasets.'''

    # Get a list of all the site's organizations from CKAN, sorted by number of
    # datasets.
    organizations = toolkit.get_action('organization_list')(
        data_dict={'sort': 'packages desc', 'all_fields': True})

    # Truncate the list to the 10 most popular organizations only.
    organizations = organizations[:10]

    return organizations

def random_app():
    '''Return a random app to feature on the homepage.'''
    
    app = toolkit.get_action('related_list')(
        data_dict={'type': 'Application', 'all_fields': True})

    import random
    random.shuffle(app)
    app = app[:1]

    return app


class GongioPlugin(plugins.SingletonPlugin):
    '''Gong.io theme plugin.

    '''
    plugins.implements(plugins.IConfigurer)

    # Declare that this plugin will implement ITemplateHelpers.
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'gongio')

    def get_helpers(self):
        '''Register the most_popular_organizations() function above as a template
        helper function.

        '''
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {'gongio_random_app': random_app, 'gongio_most_popular_organizations': most_popular_organizations}
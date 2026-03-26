<?php
/**
 * Plugin Name:       Full AWS SDK
 * Plugin URI:        https://github.com/mandato-wordpress/aws-sdk
 * Description:       Bundles the AWS SDK for PHP and exposes its autoloader so other plugins and themes can use AWS services without managing their own copy.
 * Version:           3.374.0
 * Requires at least: 5.8
 * Requires PHP:      8.2
 * Author:            amandato
 * Author URI:        https://github.com/mandato-wordpress
 * License:           GPL-2.0-or-later
 * License URI:       https://www.gnu.org/licenses/gpl-2.0.html
 * Text Domain:       full-aws-sdk
 */

defined( 'ABSPATH' ) || exit;

define( 'FULL_AWS_SDK_VERSION',     '3.374.0' );
define( 'FULL_AWS_SDK_RELEASE_DATE', '2026-03-25' );
define( 'FULL_AWS_SDK_FILE',         __FILE__ );
define( 'FULL_AWS_SDK_DIR',          plugin_dir_path( __FILE__ ) );

/**
 * Load the Composer-generated autoloader.
 * Once loaded, any code in WordPress (plugins, themes) can instantiate
 * AWS SDK clients directly, e.g. new \Aws\S3\S3Client([...])
 */
if ( ! class_exists( 'Aws\\Sdk' ) && file_exists( FULL_AWS_SDK_DIR . 'vendor/autoload.php' ) ) {
    require_once FULL_AWS_SDK_DIR . 'vendor/autoload.php';
}

/**
 * Register the admin page under Tools.
 */
add_action( 'admin_menu', 'full_aws_sdk_register_admin_page' );

function full_aws_sdk_register_admin_page() {
    add_management_page(
        __( 'AWS SDK', 'full-aws-sdk' ),       // Page title
        __( 'AWS SDK', 'full-aws-sdk' ),       // Menu title
        'manage_options',                  // Capability
        'full-aws-sdk',                         // Menu slug
        'full_aws_sdk_render_admin_page'    // Callback
    );
}

/**
 * Render the admin page.
 */
function full_aws_sdk_render_admin_page() {
    if ( ! current_user_can( 'manage_options' ) ) {
        wp_die( esc_html__( 'You do not have sufficient permissions to access this page.', 'full-aws-sdk' ) );
    }

    $sdk_version      = FULL_AWS_SDK_VERSION;
    $sdk_release_date = FULL_AWS_SDK_RELEASE_DATE;
    $autoloader_path  = FULL_AWS_SDK_DIR . 'vendor/autoload.php';
    $autoloader_ok    = file_exists( $autoloader_path );

    ?>
    <div class="wrap aws-sdk-wrap">
        <h1>
            <span class="dashicons dashicons-cloud" style="font-size:30px;vertical-align:top;margin-right:8px;color:#ff9900;"></span>
            <?php esc_html_e( 'Full AWS SDK', 'full-aws-sdk' ); ?>
        </h1>

        <div class="aws-sdk-status-cards" style="display:flex;gap:20px;flex-wrap:wrap;margin-top:20px;">

            <div class="aws-sdk-card" style="background:#fff;border:1px solid #c3c4c7;border-radius:4px;padding:20px 24px;min-width:220px;box-shadow:0 1px 2px rgba(0,0,0,.07);">
                <h2 style="margin-top:0;font-size:14px;text-transform:uppercase;color:#646970;letter-spacing:.5px;">
                    <?php esc_html_e( 'SDK Version', 'full-aws-sdk' ); ?>
                </h2>
                <p style="font-size:28px;font-weight:700;margin:8px 0 0;color:#1d2327;">
                    <?php echo esc_html( $sdk_version ); ?>
                </p>
            </div>

            <div class="aws-sdk-card" style="background:#fff;border:1px solid #c3c4c7;border-radius:4px;padding:20px 24px;min-width:220px;box-shadow:0 1px 2px rgba(0,0,0,.07);">
                <h2 style="margin-top:0;font-size:14px;text-transform:uppercase;color:#646970;letter-spacing:.5px;">
                    <?php esc_html_e( 'Release Date', 'full-aws-sdk' ); ?>
                </h2>
                <p style="font-size:28px;font-weight:700;margin:8px 0 0;color:#1d2327;">
                    <?php echo esc_html( date_i18n( get_option( 'date_format' ), strtotime( $sdk_release_date ) ) ); ?>
                </p>
            </div>

            <div class="aws-sdk-card" style="background:#fff;border:1px solid #c3c4c7;border-radius:4px;padding:20px 24px;min-width:220px;box-shadow:0 1px 2px rgba(0,0,0,.07);">
                <h2 style="margin-top:0;font-size:14px;text-transform:uppercase;color:#646970;letter-spacing:.5px;">
                    <?php esc_html_e( 'Autoloader', 'full-aws-sdk' ); ?>
                </h2>
                <?php if ( $autoloader_ok ) : ?>
                    <p style="font-size:16px;font-weight:600;margin:8px 0 0;color:#00a32a;">
                        <span class="dashicons dashicons-yes-alt" style="vertical-align:middle;"></span>
                        <?php esc_html_e( 'Active', 'full-aws-sdk' ); ?>
                    </p>
                <?php else : ?>
                    <p style="font-size:16px;font-weight:600;margin:8px 0 0;color:#d63638;">
                        <span class="dashicons dashicons-warning" style="vertical-align:middle;"></span>
                        <?php esc_html_e( 'Not found – run composer install', 'full-aws-sdk' ); ?>
                    </p>
                <?php endif; ?>
            </div>

        </div><!-- .aws-sdk-status-cards -->

        <div style="background:#fff;border:1px solid #c3c4c7;border-radius:4px;padding:20px 24px;margin-top:20px;box-shadow:0 1px 2px rgba(0,0,0,.07);">
            <h2 style="margin-top:0;"><?php esc_html_e( 'Using the SDK in Your Plugin or Theme', 'full-aws-sdk' ); ?></h2>
            <p><?php esc_html_e( 'The autoloader is registered automatically when this plugin is active. You can use any AWS SDK client without any additional setup:', 'full-aws-sdk' ); ?></p>
            <pre style="background:#1d2327;color:#f0f0f1;padding:16px;border-radius:4px;overflow:auto;font-size:13px;"><code>&lt;?php
// Confirm the AWS SDK plugin is active before using it.
if ( class_exists( 'Aws\\S3\\S3Client' ) && class_exists( 'Aws\\CloudFront\\CloudFrontClient' ) ) {
    $s3 = new \Aws\S3\S3Client([
        'region'  =&gt; 'us-east-1',
        'version' =&gt; 'latest',
    ]);

    $cf = new \Aws\CloudFront\CloudFrontClient([
        'region'  =&gt; 'us-east-1',
        'version' =&gt; 'latest',
    ]);
}</code></pre>
            <p>
                <a href="https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/welcome.html" target="_blank" rel="noopener noreferrer" class="button button-secondary">
                    <?php esc_html_e( 'AWS SDK for PHP Documentation', 'full-aws-sdk' ); ?>
                </a>
            </p>
        </div>

        <div style="background:#fff;border:1px solid #c3c4c7;border-radius:4px;padding:20px 24px;margin-top:20px;box-shadow:0 1px 2px rgba(0,0,0,.07);">
            <h2 style="margin-top:0;"><?php esc_html_e( 'Included AWS Services', 'full-aws-sdk' ); ?></h2>
            <p><?php esc_html_e( 'This plugin bundles the full AWS SDK for PHP. Commonly used services include:', 'full-aws-sdk' ); ?></p>
            <ul style="columns:3;list-style:disc;padding-left:20px;">
                <?php
                $services = [
                    'S3 – Simple Storage Service',
                    'EC2 – Elastic Compute Cloud',
                    'CloudFront – CDN',
                    'Lambda – Serverless Functions',
                    'SES – Simple Email Service',
                    'SQS – Simple Queue Service',
                    'SNS – Simple Notification Service',
                    'DynamoDB – NoSQL Database',
                    'RDS – Relational Database Service',
                    'IAM – Identity & Access Management',
                    'CloudWatch – Monitoring',
                    'Secrets Manager',
                    'Rekognition – Image Analysis',
                    'Polly – Text to Speech',
                    'Translate – Language Translation',
                    'Bedrock – Generative AI',
                ];
                foreach ( $services as $service ) {
                    echo '<li>' . esc_html( $service ) . '</li>';
                }
                ?>
            </ul>
        </div>

    </div><!-- .aws-sdk-wrap -->
    <?php
}

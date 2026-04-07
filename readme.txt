=== Full AWS SDK ===
Contributors:      amandato
Tags:              aws, sdk, s3, ec2, cloudfront
Requires at least: 5.8
Tested up to:      6.9
Requires PHP:      8.2
Stable tag:        3.376.4
Donate link:       https://angelo.mandato.com/amazon-web-services/full-aws-sdk-wordpress-plugin/
License:           GPL-2.0-or-later
License URI:       https://www.gnu.org/licenses/gpl-2.0.html

Bundles the AWS SDK for PHP and exposes its autoloader so any other plugin or theme can use AWS services without managing their own copy.

== Description ==

**Full AWS SDK** is a simple plugin that includes the latest version of the [AWS SDK for PHP](https://github.com/aws/aws-sdk-php) compatible with PHP 8.2 or newer. By activating this single plugin you give your entire WordPress installation access to every AWS service client the SDK supports — no duplicated vendor directories, no version conflicts.

= How it works =

After activation the plugin registers the Composer-generated autoloader. Any plugin or theme that runs after it can directly instantiate AWS clients:

`
<?php
if ( class_exists('Aws\\\\S3\\\\S3Client') ) {
    $s3 = new \Aws\S3\S3Client([
        'region'  => 'us-east-1',
        'version' => 'latest',
    ]);
}
`

= Supported AWS services (sample) =

* **S3** – Simple Storage Service
* **EC2** – Elastic Compute Cloud
* **CloudFront** – Content Delivery Network
* **Lambda** – Serverless Functions
* **SES** – Simple Email Service
* **SQS** – Simple Queue Service
* **SNS** – Simple Notification Service
* **DynamoDB** – NoSQL Database
* **RDS** – Relational Database Service
* **IAM** – Identity & Access Management
* **CloudWatch** – Monitoring & Observability
* **Secrets Manager** – Credential Storage
* **Rekognition** – Image & Video Analysis
* **Polly** – Text-to-Speech
* **Translate** – Machine Translation
* **Bedrock** - Generative AI Using Foundation Models

= Plugin versioning =

The plugin version always matches the bundled AWS SDK for PHP version.

= Developer usage =

**Check that the plugin is active before using the SDK:**

`
if ( !class_exists('Aws\\\\Sdk') ) {
    // Show admin notice asking the user to install PHP AWS SDK plugin.
    return;
}
`

**Declare a plugin dependency (recommended):**

Add the following to your plugin headers so WordPress can warn users when this plugin is missing:

`
Requires Plugins: php-aws-sdk
`

== Installation ==

1. Upload the `aws-sdk` folder to `/wp-content/plugins/`.
2. Activate the plugin through the **Plugins** screen in WordPress.
3. Visit **Tools → AWS SDK** to verify the SDK version and autoloader status.

No API keys are required by this plugin itself — individual plugins and themes are responsible for supplying their own AWS credentials.

== Frequently Asked Questions ==

= Do I need AWS credentials to use this plugin? =

No. This plugin only loads the SDK autoloader. Credentials are configured by whatever plugin or theme actually calls the AWS APIs.

= Can I use this plugin alongside another plugin that also bundles the AWS SDK? =

It is best practice to have only one copy of the SDK loaded. Check for `defined('AWS_SDK_WP_VERSION')` before loading your own copy.

= Does this plugin call any AWS services itself? =

No. It only registers the autoloader and renders the admin information page.

= How do I update the SDK? =

The plugin version mirrors the AWS SDK for PHP version. Install the latest plugin update to get the latest SDK.

= Will this work with PHP 8.x? =

Yes. PHP 8.2 or higher is required. The AWS SDK for PHP 3.x fully supports PHP 8.2 and newer.

= What determines which version of PHP is supported? =

The minimum version requirements are set by the [AWS SDK for PHP](https://github.com/aws/aws-sdk-php), and its dependencies including Symfony. Currently Symfony 7.4 requires PHP 8.2 or newer, which is why PHP 8.2 is currently the minimum version. Symfony 7.4 is an LTS (Long Term Support) edition, and will include bug fixes until  November 2028 and security support until November 2029.

== Screenshots ==

1. Full AWS SDK information page in the WordPress Admin > Tools menu.
2. The **Tools → AWS SDK** admin page showing the bundled SDK version, release date, and usage examples.


== Changelog ==

For the full history see [CHANGELOG.md](https://github.com/mandato-wordpress/full-aws-sdk/blob/main/CHANGELOG.md).

= 3.376.4 =
* Updated bundled Full AWS SDK plugin for WordPress to 3.376.4 (released 2026-04-06).

= 3.376.3 =
* Updated bundled Full AWS SDK plugin for WordPress to 3.376.3 (released 2026-04-03).

= 3.376.2 =
* Updated bundled Full AWS SDK plugin for WordPress to 3.376.2 (released 2026-04-02).


== Upgrade Notice ==

= 3.373.8 =
Initial release. Install to make the AWS SDK for PHP available to all plugins and themes on your site.

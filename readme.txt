=== AWS SDK for WordPress ===
Contributors:      amandato
Tags:              aws, sdk, amazon, s3, ec2, cloudfront, lambda
Requires at least: 5.8
Tested up to:      6.9
Requires PHP:      8.2
Stable tag:        3.374.0
License:           GPL-2.0-or-later
License URI:       https://www.gnu.org/licenses/gpl-2.0.html

Bundles the AWS SDK for PHP and exposes its autoloader so any other plugin or theme can use AWS services without managing their own SDK copy.

== Description ==

**AWS SDK for WordPress** is a lightweight plugin that acts as a shared host for the [AWS SDK for PHP](https://github.com/aws/aws-sdk-php). By activating this single plugin you give your entire WordPress installation access to every AWS service client the SDK supports — no duplicated vendor directories, no version conflicts.

= How it works =

After activation the plugin registers the Composer-generated autoloader. Any plugin or theme that runs after it can directly instantiate AWS clients:

`
<?php
if ( defined( 'AWS_SDK_WP_VERSION' ) ) {
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

= Plugin versioning =

The plugin version always matches the bundled AWS SDK for PHP version. A GitHub Actions workflow checks for new SDK releases once per day, automatically commits the updated vendor directory, and publishes a new release.

= Developer usage =

**Check that the plugin is active before using the SDK:**

`
if ( ! defined( 'AWS_SDK_WP_VERSION' ) ) {
    // Show admin notice asking the user to install AWS SDK for WordPress.
    return;
}
`

**Declare a plugin dependency (recommended):**

Add the following to your plugin headers so WordPress can warn users when this plugin is missing:

`
Requires Plugins: aws-sdk
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

Yes. PHP 8.2 or higher is required. The AWS SDK for PHP 3.x fully supports PHP 8.2 and 8.3.

== Screenshots ==

1. The **Tools → AWS SDK** admin page showing the bundled SDK version, release date, and usage examples.

== Changelog ==

For the full history see [CHANGELOG.md](https://github.com/mandato-wordpress/aws-sdk/blob/main/CHANGELOG.md).

= 3.374.0 =
* Updated bundled AWS SDK for PHP to 3.374.0 (released 2026-03-25).

= 3.373.9 =
* Updated bundled AWS SDK for PHP to 3.373.9 (released 2026-03-24).

= 3.373.8 =
* Initial release bundling AWS SDK for PHP 3.373.8 (released 2026-03-23).



== Upgrade Notice ==

= 3.373.8 =
Initial release. Install to make the AWS SDK for PHP available to all plugins and themes on your site.
